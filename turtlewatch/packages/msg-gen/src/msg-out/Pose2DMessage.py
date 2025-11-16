from dataclasses import dataclass


@dataclass
class Pose2DMessage:
    x: float
    y: float
    theta: float
