from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .PoseMessage import PoseMessage
from .PointMessage import PointMessage
from .HeaderMessage import HeaderMessage

@dataclass
class InteractiveMarkerFeedbackMessage(genpy.Message):
    _type: str # topic type \cmd_vel
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

    __slots__ = ['header', 'client_id', 'marker_name', 'control_name', 'KEEP_ALIVE', 'POSE_UPDATE', 'MENU_SELECT', 'BUTTON_CLICK', 'MOUSE_DOWN', 'MOUSE_UP', 'event_type', 'pose', 'menu_entry_id', 'mouse_point', 'mouse_point_valid']
    _slot_types = ['Header', 'string', 'string', 'string', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'geometry_msgs/Pose', 'uint32', 'geometry_msgs/Point', 'bool']
    _has_header: bool = False
    _md5sum = "fa659e7146660d412b02fecc54bf7540"
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
    