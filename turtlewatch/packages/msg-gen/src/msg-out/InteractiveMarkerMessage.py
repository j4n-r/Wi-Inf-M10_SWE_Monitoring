from dataclasses import dataclass
from .InteractiveMarkerControlMessage import InteractiveMarkerControlMessage
from .PoseMessage import PoseMessage
from .MenuEntryMessage import MenuEntryMessage
from .HeaderMessage import HeaderMessage


@dataclass
class InteractiveMarkerMessage:
    header: HeaderMessage
    pose: PoseMessage
    name: str
    description: str
    scale: float
    menu_entries: list[MenuEntryMessage]
    controls: list[InteractiveMarkerControlMessage]
