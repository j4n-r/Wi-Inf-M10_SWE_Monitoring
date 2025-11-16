from dataclasses import dataclass
from .InteractiveMarkerControlMessage import InteractiveMarkerControlMessage
from .geometry_msgs/PoseMessage import geometry_msgs/PoseMessage
from .MenuEntryMessage import MenuEntryMessage
from .HeaderMessage import HeaderMessage

@dataclass
class InteractiveMarkerMessage:
    header: HeaderMessage
    pose: geometry_msgs/PoseMessage
    name: str
    description: str
    scale: float
    menu_entries: list[MenuEntryMessage]
    controls: list[InteractiveMarkerControlMessage]

    