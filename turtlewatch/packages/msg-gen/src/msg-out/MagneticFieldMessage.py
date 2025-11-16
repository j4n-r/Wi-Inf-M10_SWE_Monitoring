from dataclasses import dataclass
from .geometry_msgs/Vector3Message import geometry_msgs/Vector3Message
from .HeaderMessage import HeaderMessage

@dataclass
class MagneticFieldMessage:
    header: HeaderMessage
    magnetic_field: geometry_msgs/Vector3Message
    magnetic_field_covariance: list[float]

    