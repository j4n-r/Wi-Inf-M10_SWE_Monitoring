from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .QuaternionMessage import QuaternionMessage
from .MarkerMessage import MarkerMessage

@dataclass
class InteractiveMarkerControlMessage(genpy.Message):
    _type: str # topic type \cmd_vel
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

    __slots__ = ['name', 'orientation', 'INHERIT', 'FIXED', 'VIEW_FACING', 'orientation_mode', 'NONE', 'MENU', 'BUTTON', 'MOVE_AXIS', 'MOVE_PLANE', 'ROTATE_AXIS', 'MOVE_ROTATE', 'MOVE_3D', 'ROTATE_3D', 'MOVE_ROTATE_3D', 'interaction_mode', 'always_visible', 'markers', 'independent_marker_orientation', 'description']
    _slot_types = ['string', 'geometry_msgs/Quaternion', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'bool', 'Marker', 'bool', 'string']
    _has_header: bool = False
    _md5sum = "d2485a9d59140914d075b03ff308829f"
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
    