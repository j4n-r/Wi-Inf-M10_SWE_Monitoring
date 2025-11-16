from dataclasses import dataclass
from .Vector3Message import Vector3Message


@dataclass
class InertiaMessage:
    m: float
    com: Vector3Message
    ixx: float
    ixy: float
    ixz: float
    iyy: float
    iyz: float
    izz: float
