from dataclasses import dataclass
from .geometry_msgs/PoseMessage import geometry_msgs/PoseMessage
from .HeaderMessage import HeaderMessage

@dataclass
class InteractiveMarkerPoseMessage:
    header: HeaderMessage
    pose: geometry_msgs/PoseMessage
    name: str

    