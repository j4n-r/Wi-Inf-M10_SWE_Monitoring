from dataclasses import dataclass
from .geometry_msgs/Vector3Message import geometry_msgs/Vector3Message

@dataclass
class InertiaMessage:
    m: float
    com: geometry_msgs/Vector3Message
    ixx: float
    ixy: float
    ixz: float
    iyy: float
    iyz: float
    izz: float

    