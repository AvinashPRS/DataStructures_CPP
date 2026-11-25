"""
Camera / LiDAR late fusion + simple 2D Kalman-filter tracker.

This example deliberately exposes the core math, but a production AV tracker would
upgrade several pieces:

    1. Full T_{camera<-lidar} extrinsic calibration
    2. Project complete 3D LiDAR boxes, not just centers
    3. 2D/3D IoU + appearance embeddings
    4. Hungarian / JPDA / MHT instead of greedy assignment
    5. Ego-motion compensation
    6. Asynchronous camera/LiDAR timestamps
    7. EKF/UKF for nonlinear camera measurements
    8. CV/CA/CTRV IMM motion models
    9. Proper Q(dt) from acceleration-noise model
    10. Joseph-form covariance update
    11. Class probability history
    12. Occlusion reasoning

That is the direction I would take for a real autonomous-driving tracker:
one persistent 3D state, LiDAR measurement model h_L(x), camera measurement
model h_C(x), asynchronous updates, ego-motion compensation, covariance gating,
and JPDA/MHT association rather than forcing every camera frame to have a paired
LiDAR detection.
"""
import math
from dataclasses import dataclass


def f3(v):
    """Mimic `cout << fixed << setprecision(3)` for doubles."""
    return f"{v:.3f}"


# ============================================================
# 1. Basic structures
# ============================================================

@dataclass
class Vec2:
    x: float = 0.0
    y: float = 0.0


@dataclass
class CameraDetection:
    id: int
    # 2D bounding box
    umin: float
    vmin: float
    umax: float
    vmax: float
    objectClass: str
    confidence: float

    def centerU(self):
        return (self.umin + self.umax) / 2.0

    def centerV(self):
        return (self.vmin + self.vmax) / 2.0


@dataclass
class LidarDetection:
    id: int
    # Position in ego frame
    x: float
    y: float
    z: float
    # 3D bounding-box dimensions
    length: float
    width: float
    height: float
    yaw: float
    objectClass: str
    confidence: float


@dataclass
class FusedDetection:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    length: float = 0.0
    width: float = 0.0
    height: float = 0.0
    yaw: float = 0.0
    objectClass: str = ""
    confidence: float = 0.0
    cameraId: int = 0
    lidarId: int = 0


# ============================================================
# 2. Camera model
# ============================================================

@dataclass
class CameraIntrinsics:
    fx: float = 0.0
    fy: float = 0.0
    cx: float = 0.0
    cy: float = 0.0


# ------------------------------------------------------------
# Simplified ego -> camera transform
#
# Ego:    x = forward, y = left, z = up
# Camera: X = right,   Y = down, Z = forward
#
# Therefore:
#   Xc = -y_ego
#   Yc = -z_ego
#   Zc =  x_ego
#
# Depending on your convention, the sign of y may differ.
# ------------------------------------------------------------

def projectLidarToCamera(lidar, K):
    Xc = -lidar.y
    Yc = -lidar.z
    Zc = lidar.x

    if Zc <= 0.1:
        return Vec2(-1, -1)

    u = K.fx * Xc / Zc + K.cx
    v = K.fy * Yc / Zc + K.cy
    return Vec2(u, v)


# ============================================================
# 3. Camera/LiDAR association
# ============================================================

def imageDistance(cam, projectedLidar):
    du = cam.centerU() - projectedLidar.x
    dv = cam.centerV() - projectedLidar.y
    return math.sqrt(du * du + dv * dv)


def fuseCameraLidar(cameras, lidars, K):
    result = []
    cameraUsed = [False] * len(cameras)

    for lidar in lidars:
        pixel = projectLidarToCamera(lidar, K)

        print(f"\nLiDAR detection {lidar.id} projected to pixel = "
              f"({f3(pixel.x)}, {f3(pixel.y)})")

        bestCamera = -1
        bestDistance = float("inf")

        for i, cam in enumerate(cameras):
            if cameraUsed[i]:
                continue
            # Class gating
            if cam.objectClass != lidar.objectClass:
                continue
            d = imageDistance(cam, pixel)
            print(f"  distance to camera detection {cam.id} = {f3(d)} pixels")

            if d < bestDistance:
                bestDistance = d
                bestCamera = i

        # Pixel gate
        MAX_PIXEL_DISTANCE = 80.0
        if bestCamera >= 0 and bestDistance < MAX_PIXEL_DISTANCE:
            cam = cameras[bestCamera]
            cameraUsed[bestCamera] = True

            f = FusedDetection()
            # Metric geometry comes primarily from LiDAR
            f.x, f.y, f.z = lidar.x, lidar.y, lidar.z
            f.length = lidar.length
            f.width = lidar.width
            f.height = lidar.height
            f.yaw = lidar.yaw

            # Semantic class from camera
            f.objectClass = cam.objectClass

            # Simple confidence combination
            f.confidence = 1.0 - (1.0 - cam.confidence) * (1.0 - lidar.confidence)

            f.cameraId = cam.id
            f.lidarId = lidar.id
            result.append(f)

            print(f"  MATCHED with Camera {cam.id}")

    return result


# ============================================================
# 4. Simple 2D Kalman Filter
#
# State:       x = [px, py, vx, vy]
# Measurement: z = [px, py]
# ============================================================

class KalmanFilter2D:
    def __init__(self, px, py):
        # state
        self.x = [px, py, 0.0, 0.0]
        # process noise
        self.q = 0.5
        # measurement noise
        self.r = 0.25

        # Initial covariance
        self.P = [[0.0] * 4 for _ in range(4)]
        self.P[0][0] = 1.0
        self.P[1][1] = 1.0
        # High initial velocity uncertainty
        self.P[2][2] = 25.0
        self.P[3][3] = 25.0

    # --------------------------------------------------------
    # Prediction
    #
    # F = [1 0 dt 0 ]
    #     [0 1 0  dt]
    #     [0 0 1  0 ]
    #     [0 0 0  1 ]
    # --------------------------------------------------------
    def predict(self, dt):
        x, P = self.x, self.P

        # State prediction
        x[0] += x[2] * dt
        x[1] += x[3] * dt

        F = [
            [1, 0, dt, 0],
            [0, 1, 0, dt],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]

        # temp = F * P
        temp = [[0.0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    temp[i][j] += F[i][k] * P[k][j]

        # newP = temp * F^T
        newP = [[0.0] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    newP[i][j] += temp[i][k] * F[j][k]

        # Simple process noise
        for i in range(4):
            newP[i][i] += self.q

        self.P = newP

    # --------------------------------------------------------
    # Measurement update
    #
    # z = [px, py]
    # H = [1 0 0 0]
    #     [0 1 0 0]
    # --------------------------------------------------------
    def update(self, measuredX, measuredY):
        x, P, r = self.x, self.P, self.r

        # Innovation
        innovation = [measuredX - x[0], measuredY - x[1]]

        # S = HPH' + R   (H simply selects px, py)
        S00 = P[0][0] + r
        S01 = P[0][1]
        S10 = P[1][0]
        S11 = P[1][1] + r

        # inverse of 2x2 S
        det = S00 * S11 - S01 * S10
        invS = [
            [S11 / det, -S01 / det],
            [-S10 / det, S00 / det],
        ]

        # K = P H' S^-1   (P H' = first two columns of P)
        K = [[0.0, 0.0] for _ in range(4)]
        for i in range(4):
            K[i][0] = P[i][0] * invS[0][0] + P[i][1] * invS[1][0]
            K[i][1] = P[i][0] * invS[0][1] + P[i][1] * invS[1][1]

        # State update
        for i in range(4):
            x[i] += K[i][0] * innovation[0] + K[i][1] * innovation[1]

        # P = (I-KH)P
        oldP = [row[:] for row in P]
        for i in range(4):
            for j in range(4):
                P[i][j] = oldP[i][j] - K[i][0] * oldP[0][j] - K[i][1] * oldP[1][j]

    # --------------------------------------------------------
    # Mahalanobis distance for track association
    # --------------------------------------------------------
    def mahalanobis(self, measuredX, measuredY):
        x, P, r = self.x, self.P, self.r
        dx = measuredX - x[0]
        dy = measuredY - x[1]

        S00 = P[0][0] + r
        S01 = P[0][1]
        S10 = P[1][0]
        S11 = P[1][1] + r

        det = S00 * S11 - S01 * S10

        inv00 = S11 / det
        inv01 = -S01 / det
        inv10 = -S10 / det
        inv11 = S00 / det

        return dx * (inv00 * dx + inv01 * dy) + dy * (inv10 * dx + inv11 * dy)


# ============================================================
# 5. Track structure
# ============================================================

class Track:
    def __init__(self, id_, detection):
        self.id = id_
        self.objectClass = detection.objectClass
        self.kf = KalmanFilter2D(detection.x, detection.y)

        self.length = detection.length
        self.width = detection.width
        self.height = detection.height

        self.age = 1
        self.hits = 1
        self.misses = 0
        self.confirmed = False


# ============================================================
# 6. Track manager
# ============================================================

class Tracker:
    def __init__(self):
        self.tracks = []
        self.nextTrackId = 1

    def process(self, detections, dt):
        # ----------------------------------------------------
        # STEP 1: Predict all existing tracks
        # ----------------------------------------------------
        for track in self.tracks:
            track.kf.predict(dt)
            track.age += 1
            x = track.kf.x
            print(f"\nPredicted Track {track.id}: x={f3(x[0])} y={f3(x[1])} "
                  f"vx={f3(x[2])} vy={f3(x[3])}")

        # ----------------------------------------------------
        # STEP 2: Greedy association for demonstration.
        # Production system: Hungarian / JPDA / MHT.
        # ----------------------------------------------------
        detectionUsed = [False] * len(detections)

        for track in self.tracks:
            bestDetection = -1
            bestDistance = float("inf")

            for j, det in enumerate(detections):
                if detectionUsed[j]:
                    continue
                if track.objectClass != det.objectClass:
                    continue

                d2 = track.kf.mahalanobis(det.x, det.y)
                print(f"Track {track.id} -> Detection {j} Mahalanobis d^2 = {f3(d2)}")

                if d2 < bestDistance:
                    bestDistance = d2
                    bestDetection = j

            # 2D 95% chi-square gate: chi-square(2,0.95) ~= 5.991
            GATE = 5.991

            if bestDetection >= 0 and bestDistance < GATE:
                d = detections[bestDetection]
                track.kf.update(d.x, d.y)

                track.length = d.length
                track.width = d.width
                track.height = d.height

                track.hits += 1
                track.misses = 0

                # Confirm after 3 hits
                if track.hits >= 3:
                    track.confirmed = True

                detectionUsed[bestDetection] = True
                print(f"Track {track.id} matched.")
            else:
                track.misses += 1
                print(f"Track {track.id} missed.")

        # ----------------------------------------------------
        # STEP 3: Create tracks from unmatched detections
        # ----------------------------------------------------
        for j, det in enumerate(detections):
            if not detectionUsed[j]:
                self.tracks.append(Track(self.nextTrackId, det))
                self.nextTrackId += 1
                print(f"Created new track {self.tracks[-1].id}")

        # ----------------------------------------------------
        # STEP 4: Delete stale tracks
        # ----------------------------------------------------
        self.tracks = [t for t in self.tracks if not t.misses > 3]

    def printTracks(self):
        print("\n==============================\n"
              "TRACKS\n"
              "==============================")
        for t in self.tracks:
            print(f"Track ID: {t.id}")
            print(f"Class: {t.objectClass}")
            print(f"Position: ({f3(t.kf.x[0])}, {f3(t.kf.x[1])})")
            print(f"Velocity: ({f3(t.kf.x[2])}, {f3(t.kf.x[3])})")
            print(f"Hits: {t.hits}")
            print(f"Misses: {t.misses}")
            print(f"Status: {'CONFIRMED' if t.confirmed else 'TENTATIVE'}\n")


# ============================================================
# 7. Main numerical example
# ============================================================

def main():
    K = CameraIntrinsics(fx=1000.0, fy=1000.0, cx=960.0, cy=540.0)
    tracker = Tracker()

    # ========================================================
    # FRAME 1
    # ========================================================
    print("\n\n========== FRAME 1 ==========")

    lidar1 = [
        LidarDetection(1, 20.0, -2.0, 0.0, 4.5, 1.8, 1.5, 0.0, "car", 0.95),
        LidarDetection(2, 30.0, 3.0, 0.0, 4.7, 1.9, 1.6, 0.0, "car", 0.93),
    ]

    # LiDAR 1: Xc = 2,  Zc = 20 -> u = 1000*(2/20)+960  = 1060
    # LiDAR 2: Xc = -3, Zc = 30 -> u = 1000*(-3/30)+960 = 860
    camera1 = [
        CameraDetection(101, 1010, 490, 1110, 590, "car", 0.97),
        CameraDetection(102, 810, 490, 910, 590, "car", 0.96),
    ]

    fused1 = fuseCameraLidar(camera1, lidar1, K)
    print(f"\nNumber of fused detections = {len(fused1)}")

    tracker.process(fused1, 0.1)
    tracker.printTracks()

    # ========================================================
    # FRAME 2
    #
    # 100 ms later.
    # Car 1 moved: 20.0 -> 21.0  (approximately 10 m/s)
    # Car 2:       30.0 -> 30.5  (approximately 5 m/s)
    # ========================================================
    print("\n\n========== FRAME 2 ==========")

    lidar2 = [
        LidarDetection(3, 21.0, -2.0, 0.0, 4.5, 1.8, 1.5, 0.0, "car", 0.96),
        LidarDetection(4, 30.5, 3.0, 0.0, 4.7, 1.9, 1.6, 0.0, "car", 0.94),
    ]

    # Expected projection:
    #   car 1: u = 1000*(2/21)+960    ~= 1055.24
    #   car 2: u = 1000*(-3/30.5)+960 ~= 861.64
    camera2 = [
        CameraDetection(103, 1005, 490, 1105, 590, "car", 0.98),
        CameraDetection(104, 812, 490, 912, 590, "car", 0.95),
    ]

    fused2 = fuseCameraLidar(camera2, lidar2, K)
    tracker.process(fused2, 0.1)
    tracker.printTracks()

    # ========================================================
    # FRAME 3
    # ========================================================
    print("\n\n========== FRAME 3 ==========")

    lidar3 = [
        LidarDetection(5, 22.0, -2.0, 0.0, 4.5, 1.8, 1.5, 0.0, "car", 0.96),
        LidarDetection(6, 31.0, 3.0, 0.0, 4.7, 1.9, 1.6, 0.0, "car", 0.94),
    ]

    camera3 = [
        CameraDetection(105, 1000, 490, 1100, 590, "car", 0.98),
        CameraDetection(106, 813, 490, 913, 590, "car", 0.96),
    ]

    fused3 = fuseCameraLidar(camera3, lidar3, K)
    tracker.process(fused3, 0.1)
    tracker.printTracks()


if __name__ == "__main__":
    main()
