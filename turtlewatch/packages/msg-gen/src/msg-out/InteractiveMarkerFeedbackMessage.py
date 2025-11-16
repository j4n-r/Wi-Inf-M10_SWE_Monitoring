from dataclasses import dataclass
from .geometry_msgs/PoseMessage import geometry_msgs/PoseMessage
from .HeaderMessage import HeaderMessage
from .geometry_msgs/PointMessage import geometry_msgs/PointMessage

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
    pose: geometry_msgs/PoseMessage
    menu_entry_id: int
    mouse_point: geometry_msgs/PointMessage
    mouse_point_valid: bool

    