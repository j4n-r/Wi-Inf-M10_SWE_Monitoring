from dataclasses import dataclass
from typing import Any
import time
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

    def to_influx_point(self, tags: dict[str,str]) -> dict[str, Any]:
        return {
            "measurement" : str(self.__class__.__name__),
            "tags": tags,
            "fields": flatten_message(self, ""),
            "time": int(time.time())
            }

def flatten_message(msg: Any, prefix: str):
    result: dict[str, Any] = {}
    for k, v in msg.items():
        if isinstance(v, dict):
            new_prefix = f"{prefix}_{str(k)}" if prefix else str(k)
            result.update(flatten_message(v, new_prefix))
        else:
            key = f"{prefix}_{k}"
            result[key] = v
    return result
    