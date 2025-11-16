from dataclasses import dataclass
from .geometry_msgs/Vector3Message import geometry_msgs/Vector3Message
from .HeaderMessage import HeaderMessage
from .geometry_msgs/QuaternionMessage import geometry_msgs/QuaternionMessage

@dataclass
class ImuMessage:
    header: HeaderMessage
    orientation: geometry_msgs/QuaternionMessage
    orientation_covariance: list[float]
    angular_velocity: geometry_msgs/Vector3Message
    angular_velocity_covariance: list[float]
    linear_acceleration: geometry_msgs/Vector3Message
    linear_acceleration_covariance: list[float]

    