from dataclasses import dataclass
from .geometry_msgs/TwistMessage import geometry_msgs/TwistMessage
from .geometry_msgs/TransformMessage import geometry_msgs/TransformMessage

@dataclass
class MultiDOFJointTrajectoryPointMessage:
    transforms: list[geometry_msgs/TransformMessage]
    velocities: list[geometry_msgs/TwistMessage]
    accelerations: list[geometry_msgs/TwistMessage]
    time_from_start: int

    