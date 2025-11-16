from dataclasses import dataclass
from .Vector3Message import Vector3Message
from .HeaderMessage import HeaderMessage


@dataclass
class MagneticFieldMessage:
    header: HeaderMessage
    magnetic_field: Vector3Message
    magnetic_field_covariance: list[float]
