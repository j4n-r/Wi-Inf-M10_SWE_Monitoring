from dataclasses import dataclass
from .PointMessage import PointMessage
from .QuaternionMessage import QuaternionMessage


@dataclass
class PoseMessage:
    position: PointMessage
    orientation: QuaternionMessage
