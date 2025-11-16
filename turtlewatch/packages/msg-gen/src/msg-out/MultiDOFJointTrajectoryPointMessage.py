from dataclasses import dataclass
from .TwistMessage import TwistMessage
from .TransformMessage import TransformMessage


@dataclass
class MultiDOFJointTrajectoryPointMessage:
    transforms: list[TransformMessage]
    velocities: list[TwistMessage]
    accelerations: list[TwistMessage]
    time_from_start: int
