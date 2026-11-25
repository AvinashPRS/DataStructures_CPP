"""
15-state Error-State EKF Pose Estimator (Python / numpy port of pose_estimator.cpp)

Run:
    python3 pose_estimator.py

Nominal state:
  p_W   : position in world frame
  v_W   : velocity in world frame
  R_WE  : rotation Ego -> World
  ba    : accelerometer bias
  bg    : gyroscope bias

Error state:
  dx = [dp, dv, dtheta, dba, dbg]^T

IMU:
  gyro  = omega + bg + ng
  accel = specific_force + ba + na

Other measurements:
  GNSS position
  wheel longitudinal velocity

Coordinate convention:
  World Z is UP
  gravity = [0, 0, -9.81]
"""
import bisect
import math
import sys
from dataclasses import dataclass, field

import numpy as np

STATE_SIZE = 15


# ============================================================
# Utility: skew symmetric matrix
# skew(a) @ b = a x b
# ============================================================
def skew(v):
    return np.array([
        [0.0, -v[2], v[1]],
        [v[2], 0.0, -v[0]],
        [-v[1], v[0], 0.0],
    ])


# ============================================================
# SO(3) exponential map: rotation vector phi -> rotation matrix
# ============================================================
def expSO3(phi):
    theta = np.linalg.norm(phi)
    A = skew(phi)
    if theta < 1e-8:
        # First/second order approximation
        return np.eye(3) + A + 0.5 * A @ A

    a = math.sin(theta) / theta
    b = (1.0 - math.cos(theta)) / (theta * theta)
    return np.eye(3) + a * A + b * A @ A


# ============================================================
# SO(3) logarithm
# ============================================================
def logSO3(R):
    cosTheta = (np.trace(R) - 1.0) * 0.5
    cosTheta = min(max(cosTheta, -1.0), 1.0)
    theta = math.acos(cosTheta)

    w = np.array([
        R[2, 1] - R[1, 2],
        R[0, 2] - R[2, 0],
        R[1, 0] - R[0, 1],
    ])
    if theta < 1e-8:
        return 0.5 * w

    return theta / (2.0 * math.sin(theta)) * w


# ============================================================
# Re-orthogonalize rotation matrix
# Numerical integration can slowly violate R^T R = I.
# ============================================================
def normalizeRotation(R):
    U, _, Vt = np.linalg.svd(R)
    result = U @ Vt
    if np.linalg.det(result) < 0:
        U[:, 2] *= -1.0
        result = U @ Vt
    return result


# ============================================================
# Homogeneous SE(3) pose
# ============================================================
def makePose(R_WE, p_W):
    T = np.eye(4)
    T[0:3, 0:3] = R_WE
    T[0:3, 3] = p_W
    return T


# ============================================================
# Minimal quaternion helpers (replacement for Eigen::Quaterniond)
# Quaternions are stored as numpy arrays [w, x, y, z].
# ============================================================
def quatFromRotation(R):
    tr = np.trace(R)
    if tr > 0.0:
        s = math.sqrt(tr + 1.0) * 2.0
        w = 0.25 * s
        x = (R[2, 1] - R[1, 2]) / s
        y = (R[0, 2] - R[2, 0]) / s
        z = (R[1, 0] - R[0, 1]) / s
    elif R[0, 0] > R[1, 1] and R[0, 0] > R[2, 2]:
        s = math.sqrt(1.0 + R[0, 0] - R[1, 1] - R[2, 2]) * 2.0
        w = (R[2, 1] - R[1, 2]) / s
        x = 0.25 * s
        y = (R[0, 1] + R[1, 0]) / s
        z = (R[0, 2] + R[2, 0]) / s
    elif R[1, 1] > R[2, 2]:
        s = math.sqrt(1.0 + R[1, 1] - R[0, 0] - R[2, 2]) * 2.0
        w = (R[0, 2] - R[2, 0]) / s
        x = (R[0, 1] + R[1, 0]) / s
        y = 0.25 * s
        z = (R[1, 2] + R[2, 1]) / s
    else:
        s = math.sqrt(1.0 + R[2, 2] - R[0, 0] - R[1, 1]) * 2.0
        w = (R[1, 0] - R[0, 1]) / s
        x = (R[0, 2] + R[2, 0]) / s
        y = (R[1, 2] + R[2, 1]) / s
        z = 0.25 * s
    q = np.array([w, x, y, z])
    return q / np.linalg.norm(q)


def quatToRotation(q):
    w, x, y, z = q
    return np.array([
        [1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)],
        [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)],
        [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)],
    ])


def quatSlerp(qa, qb, alpha):
    d = float(np.dot(qa, qb))
    # take the shortest path
    if d < 0.0:
        qb = -qb
        d = -d
    if d > 1.0 - 1e-12:
        q = (1.0 - alpha) * qa + alpha * qb
    else:
        theta = math.acos(d)
        s = math.sin(theta)
        q = (math.sin((1.0 - alpha) * theta) / s) * qa + (math.sin(alpha * theta) / s) * qb
    return q / np.linalg.norm(q)


# ============================================================
# Sensor data structures
# ============================================================
@dataclass
class ImuMeasurement:
    timestamp: float = 0.0
    accel: np.ndarray = field(default_factory=lambda: np.zeros(3))  # m/s^2 specific force
    gyro: np.ndarray = field(default_factory=lambda: np.zeros(3))   # rad/s


@dataclass
class GnssMeasurement:
    timestamp: float = 0.0
    position: np.ndarray = field(default_factory=lambda: np.zeros(3))
    covariance: np.ndarray = field(default_factory=lambda: np.zeros((3, 3)))


@dataclass
class WheelMeasurement:
    timestamp: float = 0.0
    longitudinalVelocity: float = 0.0
    variance: float = 0.0


# ============================================================
# Pose sample for interpolation / LiDAR deskewing
# ============================================================
@dataclass
class PoseSample:
    timestamp: float
    position: np.ndarray
    orientation: np.ndarray  # quaternion [w, x, y, z]


# ============================================================
# Nominal navigation state
# ============================================================
@dataclass
class NavigationState:
    timestamp: float = 0.0
    position: np.ndarray = field(default_factory=lambda: np.zeros(3))
    velocity: np.ndarray = field(default_factory=lambda: np.zeros(3))
    R_WE: np.ndarray = field(default_factory=lambda: np.eye(3))
    accelBias: np.ndarray = field(default_factory=lambda: np.zeros(3))
    gyroBias: np.ndarray = field(default_factory=lambda: np.zeros(3))


# ============================================================
# Error State EKF
# ============================================================
class ErrorStateEKF:
    MAX_HISTORY = 10000

    def __init__(self):
        self.state_ = NavigationState()
        self.initialized_ = False
        self.gravity_ = np.array([0.0, 0.0, -9.81])

        # Typical illustrative values.
        # These MUST be replaced with values from
        # actual IMU noise characterization/datasheet.
        self.sigmaAccel_ = 0.10
        self.sigmaGyro_ = 0.01
        self.sigmaAccelBias_ = 0.001
        self.sigmaGyroBias_ = 0.0001

        self.poseHistory_ = []

        P = np.zeros((STATE_SIZE, STATE_SIZE))
        # Initial position uncertainty
        P[0:3, 0:3] = np.eye(3) * 4.0
        # Initial velocity uncertainty
        P[3:6, 3:6] = np.eye(3) * 1.0
        # Initial attitude uncertainty, approximately 5 degrees
        attitudeSigma = 5.0 * math.pi / 180.0
        P[6:9, 6:9] = np.eye(3) * attitudeSigma * attitudeSigma
        # Accelerometer bias uncertainty
        P[9:12, 9:12] = np.eye(3) * 0.01
        # Gyro bias uncertainty
        P[12:15, 12:15] = np.eye(3) * 0.001
        self.P_ = P

    # ========================================================
    # Noise configuration
    # ========================================================
    def setNoiseParameters(self, accelNoise, gyroNoise, accelBiasNoise, gyroBiasNoise):
        self.sigmaAccel_ = accelNoise
        self.sigmaGyro_ = gyroNoise
        self.sigmaAccelBias_ = accelBiasNoise
        self.sigmaGyroBias_ = gyroBiasNoise

    # ========================================================
    # Initialization
    # ========================================================
    def initialize(self, timestamp, position, velocity, R_WE,
                   accelBias=None, gyroBias=None):
        s = self.state_
        s.timestamp = timestamp
        s.position = np.array(position, dtype=float)
        s.velocity = np.array(velocity, dtype=float)
        s.R_WE = normalizeRotation(np.array(R_WE, dtype=float))
        s.accelBias = np.zeros(3) if accelBias is None else np.array(accelBias, dtype=float)
        s.gyroBias = np.zeros(3) if gyroBias is None else np.array(gyroBias, dtype=float)

        self.initialized_ = True
        self._savePose()

    # ========================================================
    # IMU propagation
    # ========================================================
    def processImu(self, imu):
        if not self.initialized_:
            return
        s = self.state_

        dt = imu.timestamp - s.timestamp
        if dt <= 0.0:
            return

        # Avoid huge propagation if sensor stream has a gap.
        if dt > 0.1:
            print(f"Warning: large IMU dt = {dt:.6f} seconds", file=sys.stderr)

        # Bias corrected IMU
        omega = imu.gyro - s.gyroBias
        specificForce = imu.accel - s.accelBias

        # Store old rotation because acceleration measurement
        # corresponds approximately to beginning of interval.
        R_old = s.R_WE.copy()

        # World acceleration: a_W = R_WE * f_E + g_W
        accelerationWorld = R_old @ specificForce + self.gravity_

        # Position integration
        s.position = s.position + s.velocity * dt + 0.5 * accelerationWorld * dt * dt

        # Velocity integration
        s.velocity = s.velocity + accelerationWorld * dt

        # Orientation integration: R_{k+1} = R_k Exp((omega-bg) dt)
        s.R_WE = normalizeRotation(R_old @ expSO3(omega * dt))

        # Covariance propagation
        self._propagateCovariance(specificForce, omega, R_old, dt)

        s.timestamp = imu.timestamp
        self._savePose()

    # ========================================================
    # GNSS position update
    # z = p_W + noise
    # ========================================================
    def processGnss(self, gnss):
        if not self.initialized_:
            return False

        # Measurement should normally arrive after propagation
        # to approximately the same timestamp.
        predicted = self.state_.position
        residual = gnss.position - predicted

        H = np.zeros((3, STATE_SIZE))
        H[0:3, 0:3] = np.eye(3)

        S = H @ self.P_ @ H.T + gnss.covariance
        S_inv = np.linalg.inv(S)

        mahalanobis = float(residual @ S_inv @ residual)

        # 99% chi-square threshold for 3 DOF
        gate = 11.345

        print(f"GNSS Mahalanobis d^2 = {mahalanobis:.6f}")

        if mahalanobis > gate:
            print("GNSS rejected by gate")
            return False

        K = self.P_ @ H.T @ S_inv
        dx = K @ residual

        self._injectError(dx)

        # Joseph covariance update
        A = np.eye(STATE_SIZE) - K @ H
        self.P_ = A @ self.P_ @ A.T + K @ gnss.covariance @ K.T

        self._symmetrizeCovariance()
        self._savePose()
        return True

    # ========================================================
    # Wheel speed update
    # Wheel measures forward body velocity:
    # z = e_x^T R_EW v_W
    # ========================================================
    def processWheel(self, wheel):
        if not self.initialized_:
            return False

        R_EW = self.state_.R_WE.T
        velocityBody = R_EW @ self.state_.velocity

        predicted = velocityBody[0]
        residual = wheel.longitudinalVelocity - predicted

        H = np.zeros((1, STATE_SIZE))
        # derivative wrt world velocity
        H[0, 3:6] = R_EW[0, :]

        # ----------------------------------------------------
        # Approximate attitude Jacobian.
        # With right multiplicative attitude error:
        #   R_true = R_hat Exp(dtheta)
        #   R_true^T v ~ (I - [dtheta]x) R_hat^T v
        #   delta(v_body) = [v_body]x dtheta
        # ----------------------------------------------------
        Jtheta = skew(velocityBody)
        H[0, 6:9] = Jtheta[0, :]

        S = float((H @ self.P_ @ H.T)[0, 0]) + wheel.variance
        d2 = residual * residual / S

        # 99% chi-square threshold, 1 DOF
        gate = 6.635

        if d2 > gate:
            print(f"Wheel measurement rejected. d^2={d2:.6f}")
            return False

        K = self.P_ @ H.T / S          # 15x1
        dx = (K * residual).ravel()

        self._injectError(dx)

        A = np.eye(STATE_SIZE) - K @ H
        R = np.array([[wheel.variance]])
        self.P_ = A @ self.P_ @ A.T + K @ R @ K.T

        self._symmetrizeCovariance()
        return True

    # ========================================================
    # Non-holonomic constraint
    # Vehicle lateral/vertical body velocity ~= 0.
    # z = [0,0]
    # h(x) = [v_body_y, v_body_z]
    # ========================================================
    def applyNonHolonomicConstraint(self, variance=0.05):
        R_EW = self.state_.R_WE.T
        vBody = R_EW @ self.state_.velocity

        residual = np.array([-vBody[1], -vBody[2]])

        H = np.zeros((2, STATE_SIZE))
        # Velocity Jacobian
        H[0, 3:6] = R_EW[1, :]
        H[1, 3:6] = R_EW[2, :]

        # Attitude Jacobian
        Jtheta = skew(vBody)
        H[0, 6:9] = Jtheta[1, :]
        H[1, 6:9] = Jtheta[2, :]

        R = np.eye(2) * variance
        S = H @ self.P_ @ H.T + R
        S_inv = np.linalg.inv(S)

        d2 = float(residual @ S_inv @ residual)

        # 99% for 2 DOF
        if d2 > 9.210:
            return False

        K = self.P_ @ H.T @ S_inv
        dx = K @ residual

        self._injectError(dx)

        A = np.eye(STATE_SIZE) - K @ H
        self.P_ = A @ self.P_ @ A.T + K @ R @ K.T

        self._symmetrizeCovariance()
        return True

    # ========================================================
    # Accessors
    # ========================================================
    def state(self):
        return self.state_

    def covariance(self):
        return self.P_

    def pose(self):
        return makePose(self.state_.R_WE, self.state_.position)

    def poseHistory(self):
        return self.poseHistory_

    # ========================================================
    # Pose interpolation
    # Useful for LiDAR deskewing.
    # Returns the 4x4 pose T_WE, or None on failure.
    # ========================================================
    def interpolatePose(self, timestamp):
        hist = self.poseHistory_
        if not hist:
            return None

        if timestamp < hist[0].timestamp or timestamp > hist[-1].timestamp:
            return None

        # lower_bound: first sample with sample.timestamp >= timestamp
        times = [s.timestamp for s in hist]
        upper = bisect.bisect_left(times, timestamp)

        if upper == 0:
            s = hist[0]
            return makePose(quatToRotation(s.orientation), s.position)

        if upper == len(hist):
            s = hist[-1]
            return makePose(quatToRotation(s.orientation), s.position)

        b = hist[upper]
        a = hist[upper - 1]

        alpha = (timestamp - a.timestamp) / (b.timestamp - a.timestamp)

        position = (1.0 - alpha) * a.position + alpha * b.position
        orientation = quatSlerp(a.orientation, b.orientation, alpha)

        return makePose(quatToRotation(orientation), position)

    # ========================================================
    # Covariance propagation
    #
    # dx_dot = F dx + G n
    # ========================================================
    def _propagateCovariance(self, specificForce, omega, R_WE, dt):
        F = np.zeros((STATE_SIZE, STATE_SIZE))
        # dp_dot = dv
        F[0:3, 3:6] = np.eye(3)
        # dv_dot = -R [a]x dtheta - R dba - R na
        F[3:6, 6:9] = -R_WE @ skew(specificForce)
        F[3:6, 9:12] = -R_WE
        # dtheta_dot = -[omega]x dtheta - dbg - ng
        F[6:9, 6:9] = -skew(omega)
        F[6:9, 12:15] = -np.eye(3)

        # ----------------------------------------------------
        # Noise vector: n = [na, ng, nba, nbg], dimension 12
        # ----------------------------------------------------
        G = np.zeros((STATE_SIZE, 12))
        # accel noise
        G[3:6, 0:3] = -R_WE
        # gyro noise
        G[6:9, 3:6] = -np.eye(3)
        # accel bias random walk
        G[9:12, 6:9] = np.eye(3)
        # gyro bias random walk
        G[12:15, 9:12] = np.eye(3)

        Qc = np.zeros((12, 12))
        Qc[0:3, 0:3] = np.eye(3) * self.sigmaAccel_ ** 2
        Qc[3:6, 3:6] = np.eye(3) * self.sigmaGyro_ ** 2
        Qc[6:9, 6:9] = np.eye(3) * self.sigmaAccelBias_ ** 2
        Qc[9:12, 9:12] = np.eye(3) * self.sigmaGyroBias_ ** 2

        # ----------------------------------------------------
        # First-order discretization:
        #   Phi ~= I + F dt
        #   Qd  ~= G Qc G^T dt
        # For production: Van Loan or higher-order discretization is better.
        # ----------------------------------------------------
        Phi = np.eye(STATE_SIZE) + F * dt
        Qd = G @ Qc @ G.T * dt

        self.P_ = Phi @ self.P_ @ Phi.T + Qd
        self._symmetrizeCovariance()

    # ========================================================
    # Inject error-state correction into nominal state
    # ========================================================
    def _injectError(self, dx):
        dp = dx[0:3]
        dv = dx[3:6]
        dtheta = dx[6:9]
        dba = dx[9:12]
        dbg = dx[12:15]

        s = self.state_
        s.position = s.position + dp
        s.velocity = s.velocity + dv
        s.R_WE = normalizeRotation(s.R_WE @ expSO3(dtheta))
        s.accelBias = s.accelBias + dba
        s.gyroBias = s.gyroBias + dbg

        # ----------------------------------------------------
        # Error-state reset Jacobian
        #
        # After injecting dtheta into nominal orientation,
        # reset attitude error around zero.
        # First-order approximation.
        # ----------------------------------------------------
        Greset = np.eye(STATE_SIZE)
        Greset[6:9, 6:9] = np.eye(3) - 0.5 * skew(dtheta)

        self.P_ = Greset @ self.P_ @ Greset.T
        self._symmetrizeCovariance()

    def _symmetrizeCovariance(self):
        self.P_ = 0.5 * (self.P_ + self.P_.T)

    def _savePose(self):
        s = self.state_
        sample = PoseSample(
            timestamp=s.timestamp,
            position=s.position.copy(),
            orientation=quatFromRotation(s.R_WE),
        )

        # Prevent duplicate timestamps
        if self.poseHistory_ and abs(self.poseHistory_[-1].timestamp - sample.timestamp) < 1e-9:
            self.poseHistory_[-1] = sample
            return

        self.poseHistory_.append(sample)

        # Keep bounded history. Enough for short-term LiDAR deskewing.
        if len(self.poseHistory_) > self.MAX_HISTORY:
            del self.poseHistory_[:1000]


# ============================================================
# Euler angles only for display
# ============================================================
def rotationToEulerRPY(R):
    # ZYX convention: R = Rz(yaw) Ry(pitch) Rx(roll)
    pitch = math.asin(min(max(-R[2, 0], -1.0), 1.0))
    roll = math.atan2(R[2, 1], R[2, 2])
    yaw = math.atan2(R[1, 0], R[0, 0])
    return np.array([roll, pitch, yaw])


# ============================================================
# Printing helpers (mimic Eigen's stream output with fixed/6)
# ============================================================
def fmtVec(v):
    strs = [f"{x:.6f}" for x in v]
    w = max(len(s) for s in strs)
    return " ".join(s.rjust(w) for s in strs)


def fmtMat(M):
    strs = [[f"{x:.6f}" for x in row] for row in M]
    w = max(len(s) for row in strs for s in row)
    return "\n".join(" ".join(s.rjust(w) for s in row) for row in strs)


# ============================================================
# Print state
# ============================================================
def printState(estimator, label):
    x = estimator.state()
    rpy = rotationToEulerRPY(x.R_WE)
    RAD_TO_DEG = 180.0 / math.pi
    P = estimator.covariance()

    print("\n========================================\n"
          f"{label}\n"
          "========================================")
    print(f"time     : {x.timestamp:.6f}")
    print(f"position : {fmtVec(x.position)} m")
    print(f"velocity : {fmtVec(x.velocity)} m/s")
    print(f"RPY      : {fmtVec(rpy * RAD_TO_DEG)} deg")
    print(f"acc bias : {fmtVec(x.accelBias)}")
    print(f"gyro bias: {fmtVec(x.gyroBias)}")
    print(f"position stddev: {math.sqrt(P[0, 0]):.6f} "
          f"{math.sqrt(P[1, 1]):.6f} {math.sqrt(P[2, 2]):.6f} m")
    print(f"\nT_WE:\n{fmtMat(estimator.pose())}")


# ============================================================
# Demonstration
#
# Vehicle:
#   initial velocity = 10 m/s forward
#   straight road
#
# IMU:
#   stationary specific force relative to vehicle acceleration
#   is +9.81 m/s^2 in body Z because accelerometer measures
#   specific force opposing gravity.
#
# Therefore:
#   R * [0,0,9.81] + [0,0,-9.81] = 0
# so constant velocity.
# ============================================================
def main():
    estimator = ErrorStateEKF()
    estimator.setNoiseParameters(
        0.10,     # accelerometer noise
        0.01,     # gyro noise
        0.001,    # accel bias random walk
        0.0001)   # gyro bias random walk

    # ========================================================
    # Initialize
    # ========================================================
    estimator.initialize(
        0.0,
        np.array([0.0, 0.0, 0.0]),
        np.array([10.0, 0.0, 0.0]),
        np.eye(3))

    printState(estimator, "INITIAL STATE")

    # ========================================================
    # Simulate 5 seconds
    #   IMU  : 200 Hz
    #   GNSS : 10 Hz
    #   Wheel: 50 Hz
    # ========================================================
    imuDt = 0.005
    steps = int(5.0 / imuDt)

    for k in range(1, steps + 1):
        t = k * imuDt

        # ----------------------------------------------------
        # Simulated IMU
        #
        # Vehicle travels at constant velocity.
        # Specific force: f = R^T(a - g),  a = 0,  g = [0,0,-9.81]
        # therefore: f = [0,0,9.81]
        # ----------------------------------------------------
        imu = ImuMeasurement(
            timestamp=t,
            accel=np.array([0.0, 0.0, 9.81]),
            gyro=np.zeros(3),
        )
        estimator.processImu(imu)

        # ----------------------------------------------------
        # Wheel update at 50 Hz
        # ----------------------------------------------------
        if k % 4 == 0:
            wheel = WheelMeasurement(
                timestamp=t,
                longitudinalVelocity=10.0,
                variance=0.04,  # sigma = 0.2 m/s
            )
            estimator.processWheel(wheel)
            estimator.applyNonHolonomicConstraint(0.02)

        # ----------------------------------------------------
        # GNSS update at 10 Hz
        # True position: x = 10*t
        # ----------------------------------------------------
        if k % 20 == 0:
            # Add deterministic small "noise" so demonstration is repeatable.
            noiseX = 0.10 * math.sin(2.0 * t)
            noiseY = 0.08 * math.cos(1.3 * t)
            noiseZ = 0.05 * math.sin(0.7 * t)

            cov = np.zeros((3, 3))
            cov[0, 0] = 0.25
            cov[1, 1] = 0.25
            cov[2, 2] = 0.50

            gnss = GnssMeasurement(
                timestamp=t,
                position=np.array([10.0 * t + noiseX, noiseY, noiseZ]),
                covariance=cov,
            )
            estimator.processGnss(gnss)

        # Print every second
        if k % 200 == 0:
            printState(estimator, f"STATE @ {t:.6f} sec")

    # ========================================================
    # Pose interpolation example
    # This is exactly what LiDAR deskewing needs.
    # ========================================================
    lidarPointTimestamp = 4.973
    T_WE_point = estimator.interpolatePose(lidarPointTimestamp)

    if T_WE_point is not None:
        print("\n========================================\n"
              "INTERPOLATED POSE FOR LIDAR POINT\n"
              "========================================")
        print(f"timestamp = {lidarPointTimestamp:.6f}")
        print(f"T_WE(t_i):\n{fmtMat(T_WE_point)}")


if __name__ == "__main__":
    main()
