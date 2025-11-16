from dataclasses import dataclass
from .JointTrajectoryPointMessage import JointTrajectoryPointMessage
from .HeaderMessage import HeaderMessage


@dataclass
class JointTrajectoryMessage:
    header: HeaderMessage
    joint_names: list[str]
    points: list[JointTrajectoryPointMessage]
