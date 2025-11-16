from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .JointTrajectoryPointMessage import JointTrajectoryPointMessage
from .HeaderMessage import HeaderMessage

@dataclass
class JointTrajectoryMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    joint_names: list[str]
    points: list[JointTrajectoryPointMessage]

    __slots__ = ['header', 'joint_names', 'points']
    _slot_types = ['Header', 'string', 'JointTrajectoryPoint']
    _has_header: bool = False
    _md5sum = "f11f4e777df9e367b830a9cc2dceb5ed"
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
    