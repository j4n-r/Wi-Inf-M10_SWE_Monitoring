from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .WrenchMessage import WrenchMessage
from .TwistMessage import TwistMessage
from .HeaderMessage import HeaderMessage
from .TransformMessage import TransformMessage

@dataclass
class MultiDOFJointStateMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    joint_names: list[str]
    transforms: list[TransformMessage]
    twist: list[TwistMessage]
    wrench: list[WrenchMessage]

    __slots__ = ['header', 'joint_names', 'transforms', 'twist', 'wrench']
    _slot_types = ['Header', 'string', 'geometry_msgs/Transform', 'geometry_msgs/Twist', 'geometry_msgs/Wrench']
    _has_header: bool = False
    _md5sum = "5c830012f94fd42ac50a925d938e504c"
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
    