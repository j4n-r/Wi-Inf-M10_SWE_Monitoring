from dataclasses import dataclass
from .PoseMessage import PoseMessage
from .HeaderMessage import HeaderMessage


@dataclass
class InteractiveMarkerPoseMessage:
    header: HeaderMessage
    pose: PoseMessage
    name: str
