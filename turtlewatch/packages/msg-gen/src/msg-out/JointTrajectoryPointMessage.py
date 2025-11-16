from dataclasses import dataclass


@dataclass
class JointTrajectoryPointMessage:
    positions: list[float]
    velocities: list[float]
    accelerations: list[float]
    effort: list[float]
    time_from_start: int
