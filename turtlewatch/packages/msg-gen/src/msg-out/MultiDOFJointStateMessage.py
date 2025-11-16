from dataclasses import dataclass
from .geometry_msgs/TwistMessage import geometry_msgs/TwistMessage
from .geometry_msgs/WrenchMessage import geometry_msgs/WrenchMessage
from .HeaderMessage import HeaderMessage
from .geometry_msgs/TransformMessage import geometry_msgs/TransformMessage

@dataclass
class MultiDOFJointStateMessage:
    header: HeaderMessage
    joint_names: list[str]
    transforms: list[geometry_msgs/TransformMessage]
    twist: list[geometry_msgs/TwistMessage]
    wrench: list[geometry_msgs/WrenchMessage]

    