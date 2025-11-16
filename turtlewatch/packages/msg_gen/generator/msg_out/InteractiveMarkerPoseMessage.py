from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .PoseMessage import PoseMessage
from .HeaderMessage import HeaderMessage

@dataclass
class InteractiveMarkerPoseMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    pose: PoseMessage
    name: str

    __slots__ = ['header', 'pose', 'name']
    _slot_types = ['Header', 'geometry_msgs/Pose', 'string']
    _has_header: bool = False
    _md5sum = "b6f4d1f996f4b9cc7957da38cccb436e"
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
    