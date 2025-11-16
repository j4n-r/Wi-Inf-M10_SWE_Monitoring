from dataclasses import dataclass
from .Vector3Message import Vector3Message
from .QuaternionMessage import QuaternionMessage
from .HeaderMessage import HeaderMessage


@dataclass
class ImuMessage:
    header: HeaderMessage
    orientation: QuaternionMessage
    orientation_covariance: list[float]
    angular_velocity: Vector3Message
    angular_velocity_covariance: list[float]
    linear_acceleration: Vector3Message
    linear_acceleration_covariance: list[float]
