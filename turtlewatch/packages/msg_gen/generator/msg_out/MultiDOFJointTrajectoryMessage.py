from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .MultiDOFJointTrajectoryPointMessage import MultiDOFJointTrajectoryPointMessage
from .HeaderMessage import HeaderMessage

@dataclass
class MultiDOFJointTrajectoryMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    joint_names: list[str]
    points: list[MultiDOFJointTrajectoryPointMessage]

    __slots__ = ['header', 'joint_names', 'points']
    _slot_types = ['Header', 'string', 'MultiDOFJointTrajectoryPoint']
    _has_header: bool = False
    _md5sum = "e6f6a5c02846505bfa77bb89db396ea9"
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
    