from dataclasses import dataclass
from .PoseMessage import PoseMessage
from .PointMessage import PointMessage
from .HeaderMessage import HeaderMessage


@dataclass
class InteractiveMarkerFeedbackMessage:
    header: HeaderMessage
    client_id: str
    marker_name: str
    control_name: str
    KEEP_ALIVE: int
    POSE_UPDATE: int
    MENU_SELECT: int
    BUTTON_CLICK: int
    MOUSE_DOWN: int
    MOUSE_UP: int
    event_type: int
    pose: PoseMessage
    menu_entry_id: int
    mouse_point: PointMessage
    mouse_point_valid: bool
