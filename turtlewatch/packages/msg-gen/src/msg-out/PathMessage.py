from dataclasses import dataclass
from .geometry_msgs/PoseStampedMessage import geometry_msgs/PoseStampedMessage
from .HeaderMessage import HeaderMessage

@dataclass
class PathMessage:
    header: HeaderMessage
    poses: list[geometry_msgs/PoseStampedMessage]

    