"""
Autonomous-driving camera + LiDAR tracker (Python / numpy port of av_tracker.cpp)

Persistent state in WORLD frame:

    x = [X, Y, Z, Vx, Vy, Vz]^T

Features:
  * asynchronous timestamps
  * ego-motion compensation
  * LiDAR measurement model hL(x)
  * camera nonlinear measurement model hC(x)
  * EKF
  * Mahalanobis gating
  * simplified JPDA
  * track lifecycle
"""
import math
from dataclasses import dataclass, field

import numpy as np

NX = 6


def f3(v):
    """Mimic `cout << fixed << setprecision(3)`."""
    return f"{v:.3f}"


def fmtVec(v):
    """Mimic Eigen's `vec.transpose()` stream output (fixed, 3 decimals)."""
    strs = [f"{x:.3f}" for x in v]
    w = max(len(s) for s in strs)
    return " ".join(s.rjust(w) for s in strs)


# ============================================================
# 1. Sensor measurements
# ============================================================

@dataclass
class LidarMeasurement:
    timestamp: float = 0.0
    # Measurement in LiDAR/ego frame
    position: np.ndarray = field(default_factory=lambda: np.zeros(3))
    objectClass: int = 0
    # measurement covariance
    R: np.ndarray = field(default_factory=lambda: np.zeros((3, 3)))


@dataclass
class CameraMeasurement:
    timestamp: float = 0.0
    # pixel center
    pixel: np.ndarray = field(default_factory=lambda: np.zeros(2))
    objectClass: int = 0
    confidence: float = 0.0
    # measurement covariance in pixels
    R: np.ndarray = field(default_factory=lambda: np.zeros((2, 2)))


# ============================================================
# 2. Camera model
# ============================================================

@dataclass
class CameraModel:
    fx: float = 0.0
    fy: float = 0.0
    cx: float = 0.0
    cy: float = 0.0
    # Camera pose relative to ego vehicle.
    # p_camera = R_camera_ego * p_ego + t_camera_ego
    R_camera_ego: np.ndarray = field(default_factory=lambda: np.eye(3))
    t_camera_ego: np.ndarray = field(default_factory=lambda: np.zeros(3))


# ============================================================
# 3. Ego pose
#
# We assume localization provides T_world_ego:
#   p_world = R_world_ego * p_ego + t_world_ego
# ============================================================

@dataclass
class EgoPose:
    timestamp: float = 0.0
    R_world_ego: np.ndarray = field(default_factory=lambda: np.eye(3))
    t_world_ego: np.ndarray = field(default_factory=lambda: np.zeros(3))


# ============================================================
# 4. Coordinate transformations
# ============================================================

def egoToWorld(pEgo, ego):
    return ego.R_world_ego @ pEgo + ego.t_world_ego


def worldToEgo(pWorld, ego):
    return ego.R_world_ego.T @ (pWorld - ego.t_world_ego)


def worldToCamera(pWorld, ego, camera):
    # World -> Ego
    pEgo = worldToEgo(pWorld, ego)
    # Ego -> Camera
    return camera.R_camera_ego @ pEgo + camera.t_camera_ego


# ============================================================
# 5. Track
# ============================================================

class Track:
    def __init__(self, id_, objectClass_, initialPosition, time):
        self.id = id_
        self.objectClass = objectClass_
        self.timestamp = time
        self.hits = 1
        self.misses = 0
        self.confirmed = False

        self.x = np.zeros(NX)
        self.x[0:3] = initialPosition
        # Velocity initially unknown.

        self.P = np.zeros((NX, NX))
        # position uncertainty
        self.P[0, 0] = self.P[1, 1] = self.P[2, 2] = 1.0
        # velocity highly uncertain
        self.P[3, 3] = self.P[4, 4] = self.P[5, 5] = 25.0

    # ========================================================
    # 6. Prediction
    #
    # Constant velocity model
    #   X' = X + Vx dt
    #   Y' = Y + Vy dt
    #   Z' = Z + Vz dt
    # ========================================================
    def predict(self, newTimestamp):
        dt = newTimestamp - self.timestamp
        if dt <= 0.0:
            return

        F = np.eye(NX)
        F[0, 3] = dt
        F[1, 4] = dt
        F[2, 5] = dt

        # State prediction
        self.x = F @ self.x

        # -----------------------------------------------
        # Process noise: white acceleration noise model
        # -----------------------------------------------
        sigmaA = 2.0
        dt2 = dt * dt
        dt3 = dt2 * dt
        dt4 = dt2 * dt2

        Q = np.zeros((NX, NX))
        for axis in range(3):
            p = axis
            v = axis + 3
            Q[p, p] = 0.25 * dt4 * sigmaA * sigmaA
            Q[p, v] = 0.5 * dt3 * sigmaA * sigmaA
            Q[v, p] = Q[p, v]
            Q[v, v] = dt2 * sigmaA * sigmaA

        self.P = F @ self.P @ F.T + Q
        self.timestamp = newTimestamp

    def position(self):
        return self.x[0:3]

    def velocity(self):
        return self.x[3:6]


# ============================================================
# 7. LiDAR measurement model
#
# Track lives in WORLD coordinates. LiDAR measurement has already been
# ego-motion compensated and transformed into WORLD coordinates.
#
# hL(x) = [X, Y, Z]^T
# ============================================================

def lidarMeasurementModel(track):
    return track.x[0:3].copy()


def lidarJacobian():
    H = np.zeros((3, NX))
    H[0, 0] = H[1, 1] = H[2, 2] = 1.0
    return H


# ============================================================
# 8. Camera measurement model
#
# State: position in WORLD frame.
# First: World -> Ego -> Camera
# Then:
#   u = fx * Xc/Zc + cx
#   v = fy * Yc/Zc + cy
# ============================================================

def cameraMeasurementModel(track, ego, camera):
    pCamera = worldToCamera(track.position(), ego, camera)
    X, Y, Z = pCamera

    if Z <= 0.1:
        return np.array([math.nan, math.nan])

    u = camera.fx * X / Z + camera.cx
    v = camera.fy * Y / Z + camera.cy
    return np.array([u, v])


# ============================================================
# 9. Camera Jacobian
#
# dh/dp_camera:
#   [ fx/Z   0      -fx*X/Z^2 ]
#   [ 0      fy/Z   -fy*Y/Z^2 ]
#
# dp_camera/dp_world = R_camera_ego * R_world_ego^T
# ============================================================

def cameraJacobian(track, ego, camera):
    pCamera = worldToCamera(track.position(), ego, camera)
    X, Y, Z = pCamera

    Jproj = np.array([
        [camera.fx / Z, 0.0, -camera.fx * X / (Z * Z)],
        [0.0, camera.fy / Z, -camera.fy * Y / (Z * Z)],
    ])

    JworldCamera = camera.R_camera_ego @ ego.R_world_ego.T

    H = np.zeros((2, NX))
    H[:, 0:3] = Jproj @ JworldCamera
    # Camera directly observes position, not velocity.
    return H


# ============================================================
# 10. Generic EKF update
# ============================================================

def ekfUpdate(track, z, zPred, H, R):
    innovation = z - zPred
    S = H @ track.P @ H.T + R
    K = track.P @ H.T @ np.linalg.inv(S)

    track.x = track.x + K @ innovation

    # Joseph covariance form: P = (I-KH)P(I-KH)' + KRK'
    A = np.eye(NX) - K @ H
    track.P = A @ track.P @ A.T + K @ R @ K.T


# ============================================================
# 11. Mahalanobis distance
# ============================================================

def mahalanobisSquared(innovation, S):
    return float(innovation @ np.linalg.inv(S) @ innovation)


# ============================================================
# 12. LiDAR gating
# ============================================================

def lidarGateDistance(track, measurement, R):
    H = lidarJacobian()
    predicted = lidarMeasurementModel(track)
    innovation = measurement - predicted
    S = H @ track.P @ H.T + R
    return mahalanobisSquared(innovation, S)


# ============================================================
# 13. Camera gating
# ============================================================

def cameraGateDistance(track, measurement, ego, camera):
    predicted = cameraMeasurementModel(track, ego, camera)
    if not np.all(np.isfinite(predicted)):
        return math.inf

    H = cameraJacobian(track, ego, camera)
    innovation = measurement.pixel - predicted
    S = H @ track.P @ H.T + measurement.R
    return mahalanobisSquared(innovation, S)


# ============================================================
# 14. Gaussian likelihood (needed for JPDA)
#
# L ~ exp(-0.5 d^2) / sqrt((2 pi)^NZ det(S))
# ============================================================

def gaussianLikelihood(innovation, S):
    nz = len(innovation)
    d2 = mahalanobisSquared(innovation, S)
    denominator = math.sqrt((2.0 * math.pi) ** nz * np.linalg.det(S))
    return math.exp(-0.5 * d2) / denominator


# ============================================================
# 15. Simplified JPDA LiDAR update
#
# For one track, multiple measurements can lie inside its validation gate.
#   beta0  = missed detection probability
#   beta_j = probability measurement j belongs to track.
#
# NOTE: Full multi-target JPDA computes probabilities over JOINT feasible
# association events. This implementation demonstrates the numerical
# marginal-update concept.
# ============================================================

def jpdaLidarUpdate(track, measurements, R):
    H = lidarJacobian()
    predicted = lidarMeasurementModel(track)
    S = H @ track.P @ H.T + R

    # 99% chi-square gate for 3 DOF, approximately 11.345
    gate = 11.345

    candidates = []  # list of (measurement, innovation, likelihood)
    for z in measurements:
        innovation = z - predicted
        d2 = mahalanobisSquared(innovation, S)
        if d2 < gate:
            likelihood = gaussianLikelihood(innovation, S)
            candidates.append((z, innovation, likelihood))

    if not candidates:
        track.misses += 1
        return

    # --------------------------------------------------------
    # Simplified missed detection weight.
    # In production JPDA this comes from: detection probability,
    # clutter density, joint association events, etc.
    # --------------------------------------------------------
    missedWeight = 0.05
    normalization = missedWeight + sum(c[2] for c in candidates)
    beta0 = missedWeight / normalization

    weightedInnovation = np.zeros(3)

    print(f"\nJPDA Track {track.id}")
    print(f"beta0(missed) = {f3(beta0)}")

    for j, (_, innov, lik) in enumerate(candidates):
        beta = lik / normalization
        print(f"beta measurement {j} = {f3(beta)}")
        weightedInnovation += beta * innov

    # Kalman gain
    K = track.P @ H.T @ np.linalg.inv(S)
    track.x = track.x + K @ weightedInnovation

    # --------------------------------------------------------
    # Approximate JPDA covariance correction.
    # First calculate spread of possible innovations.
    # --------------------------------------------------------
    spread = np.zeros((3, 3))
    for _, innov, lik in candidates:
        beta = lik / normalization
        spread += beta * np.outer(innov, innov)
    spread -= np.outer(weightedInnovation, weightedInnovation)

    normalKFReduction = K @ S @ K.T

    track.P = track.P - (1.0 - beta0) * normalKFReduction + K @ spread @ K.T

    track.hits += 1
    track.misses = 0
    if track.hits >= 3:
        track.confirmed = True


# ============================================================
# 16. Camera EKF update
# ============================================================

def cameraUpdate(track, measurement, ego, camera):
    predicted = cameraMeasurementModel(track, ego, camera)
    if not np.all(np.isfinite(predicted)):
        return

    H = cameraJacobian(track, ego, camera)

    # gating
    innovation = measurement.pixel - predicted
    S = H @ track.P @ H.T + measurement.R
    d2 = mahalanobisSquared(innovation, S)

    # 99% chi-square, 2 DOF: 9.21
    if d2 > 9.21:
        print(f"Camera measurement rejected. d2={f3(d2)}")
        return

    print(f"Camera update accepted. d2={f3(d2)}")

    ekfUpdate(track, measurement.pixel, predicted, H, measurement.R)


# ============================================================
# 17. Track manager
# ============================================================

class Tracker:
    def __init__(self):
        self.tracks = []
        self.nextTrackId = 1

    # --------------------------------------------------------
    # Initialize from LiDAR. This is convenient because LiDAR
    # gives metric 3D position directly.
    # --------------------------------------------------------
    def createTrack(self, measurement, ego):
        worldPosition = egoToWorld(measurement.position, ego)
        self.tracks.append(Track(self.nextTrackId, measurement.objectClass,
                                 worldPosition, measurement.timestamp))
        self.nextTrackId += 1
        print(f"Created Track {self.tracks[-1].id} at world position {fmtVec(worldPosition)}")

    # ========================================================
    # Asynchronous LiDAR event
    # ========================================================
    def processLidar(self, measurements, ego):
        if not measurements:
            return

        time = measurements[0].timestamp

        print("\n================================\n"
              f"LiDAR event @ {f3(time)} sec\n"
              "================================")

        # 1. Predict every track exactly to LiDAR timestamp
        for track in self.tracks:
            track.predict(time)

        # 2. Ego-motion compensation: measurements are in ego frame,
        #    transform them into world coordinates.
        worldMeasurements = [egoToWorld(m.position, ego) for m in measurements]

        # First frame: create tracks
        if not self.tracks:
            for m in measurements:
                self.createTrack(m, ego)
            return

        # 3. JPDA: for demonstration each track sees all measurements.
        #    Mahalanobis gating inside JPDA removes implausible measurements.
        for track in self.tracks:
            R = np.eye(3) * 0.25
            jpdaLidarUpdate(track, worldMeasurements, R)

        # 4. Delete stale tracks
        self.tracks = [t for t in self.tracks if not t.misses > 5]

    # ========================================================
    # Asynchronous camera event
    # ========================================================
    def processCamera(self, measurements, ego, camera):
        if not measurements:
            return

        time = measurements[0].timestamp

        print("\n================================\n"
              f"Camera event @ {f3(time)} sec\n"
              "================================")

        # Predict tracks to camera timestamp
        for track in self.tracks:
            track.predict(time)

        # ----------------------------------------------------
        # Simplified camera association: find minimum Mahalanobis
        # distance. The same candidate-generation machinery can
        # feed JPDA or MHT instead.
        # ----------------------------------------------------
        used = [False] * len(measurements)

        for track in self.tracks:
            best = -1
            bestD2 = math.inf

            for j, m in enumerate(measurements):
                if used[j]:
                    continue
                if m.objectClass != track.objectClass:
                    continue

                d2 = cameraGateDistance(track, m, ego, camera)
                print(f"Track {track.id} -> Camera {j} d2 = {f3(d2)}")

                if d2 < bestD2:
                    bestD2 = d2
                    best = j

            if best >= 0 and bestD2 < 9.21:
                cameraUpdate(track, measurements[best], ego, camera)
                used[best] = True

    def printTracks(self):
        print("\n--------------------------------\n"
              "TRACK STATES\n"
              "--------------------------------")
        for track in self.tracks:
            print(f"Track {track.id}")
            print(f"  position world = {fmtVec(track.position())}")
            print(f"  velocity world = {fmtVec(track.velocity())}")
            print(f"  position sigma = {f3(math.sqrt(track.P[0, 0]))}, "
                  f"{f3(math.sqrt(track.P[1, 1]))}, {f3(math.sqrt(track.P[2, 2]))}")
            print(f"  status = {'CONFIRMED' if track.confirmed else 'TENTATIVE'}")


# ============================================================
# 18. Main numerical simulation
# ============================================================

def main():
    # ========================================================
    # Camera calibration
    # ========================================================
    camera = CameraModel(fx=1000.0, fy=1000.0, cx=960.0, cy=540.0)

    # --------------------------------------------------------
    # Ego coordinates:    X = forward, Y = left,  Z = up
    # Camera:             Xc = right,  Yc = down, Zc = forward
    # Therefore:
    #   Xc = -Yego
    #   Yc = -Zego
    #   Zc =  Xego
    # --------------------------------------------------------
    camera.R_camera_ego = np.array([
        [0, -1, 0],
        [0, 0, -1],
        [1, 0, 0],
    ], dtype=float)
    camera.t_camera_ego = np.zeros(3)

    tracker = Tracker()

    # ========================================================
    # t = 0.000
    # Ego vehicle is at world x = 0. Object is 20 m ahead.
    # ========================================================
    ego0 = EgoPose(0.0, np.eye(3), np.array([0.0, 0.0, 0.0]))

    lidar0 = LidarMeasurement(
        timestamp=0.0,
        position=np.array([20.0, -2.0, 0.0]),
        objectClass=1,
        R=np.eye(3) * 0.25,
    )

    tracker.processLidar([lidar0], ego0)
    tracker.printTracks()

    # ========================================================
    # t = 0.033
    # Camera arrives BEFORE next LiDAR.
    # Ego vehicle moved approximately 0.33 m.
    # ========================================================
    ego033 = EgoPose(0.033, np.eye(3), np.array([0.33, 0.0, 0.0]))

    cam033 = CameraMeasurement(
        timestamp=0.033,
        pixel=np.array([1059.0, 540.5]),  # approximate image observation
        objectClass=1,
        confidence=0.97,
        R=np.eye(2) * 4.0,
    )

    tracker.processCamera([cam033], ego033, camera)
    tracker.printTracks()

    # ========================================================
    # t = 0.066
    # Another camera event.
    # ========================================================
    ego066 = EgoPose(0.066, np.eye(3), np.array([0.66, 0.0, 0.0]))

    cam066 = CameraMeasurement(
        timestamp=0.066,
        pixel=np.array([1058.0, 540.0]),
        objectClass=1,
        confidence=0.98,
        R=np.eye(2) * 4.0,
    )

    tracker.processCamera([cam066], ego066, camera)

    # ========================================================
    # t = 0.100
    # Next LiDAR arrives. Ego moved 1 m.
    #
    # Suppose tracked car itself moved from world X = 20 to X = 21.
    # Relative LiDAR position therefore remains: 21 - 1 = 20 m ahead.
    #
    # THIS demonstrates ego-motion compensation.
    # ========================================================
    ego100 = EgoPose(0.100, np.eye(3), np.array([1.0, 0.0, 0.0]))

    lidar100 = LidarMeasurement(
        timestamp=0.100,
        position=np.array([20.0, -2.0, 0.0]),
        objectClass=1,
        R=np.eye(3) * 0.25,
    )

    # Add clutter measurement for JPDA demonstration
    clutter = LidarMeasurement(
        timestamp=0.100,
        position=np.array([20.4, -1.7, 0.1]),
        objectClass=1,
        R=np.eye(3) * 0.25,
    )

    tracker.processLidar([lidar100, clutter], ego100)
    tracker.printTracks()

    # ========================================================
    # t = 0.133
    # Camera again.
    # ========================================================
    ego133 = EgoPose(0.133, np.eye(3), np.array([1.33, 0.0, 0.0]))

    cam133 = CameraMeasurement(
        timestamp=0.133,
        pixel=np.array([1057.0, 540.0]),
        objectClass=1,
        confidence=0.98,
        R=np.eye(2) * 4.0,
    )

    tracker.processCamera([cam133], ego133, camera)
    tracker.printTracks()


if __name__ == "__main__":
    main()
