from dataclasses import dataclass
from typing import Any
import time
from .QuaternionMessage import QuaternionMessage
from .MarkerMessage import MarkerMessage

@dataclass
class InteractiveMarkerControlMessage:
    name: str
    orientation: QuaternionMessage
    INHERIT: int
    FIXED: int
    VIEW_FACING: int
    orientation_mode: int
    NONE: int
    MENU: int
    BUTTON: int
    MOVE_AXIS: int
    MOVE_PLANE: int
    ROTATE_AXIS: int
    MOVE_ROTATE: int
    MOVE_3D: int
    ROTATE_3D: int
    MOVE_ROTATE_3D: int
    interaction_mode: int
    always_visible: bool
    markers: list[MarkerMessage]
    independent_marker_orientation: bool
    description: str

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
    