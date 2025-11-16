from dataclasses import dataclass
from .MultiDOFJointTrajectoryPointMessage import MultiDOFJointTrajectoryPointMessage
from .HeaderMessage import HeaderMessage


@dataclass
class MultiDOFJointTrajectoryMessage:
    header: HeaderMessage
    joint_names: list[str]
    points: list[MultiDOFJointTrajectoryPointMessage]
