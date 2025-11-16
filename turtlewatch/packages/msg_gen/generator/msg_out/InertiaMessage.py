from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .Vector3Message import Vector3Message

@dataclass
class InertiaMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    m: float
    com: Vector3Message
    ixx: float
    ixy: float
    ixz: float
    iyy: float
    iyz: float
    izz: float

    __slots__ = ['m', 'com', 'ixx', 'ixy', 'ixz', 'iyy', 'iyz', 'izz']
    _slot_types = ['float64', 'geometry_msgs/Vector3', 'float64', 'float64', 'float64', 'float64', 'float64', 'float64']
    _has_header: bool = False
    _md5sum = "361bb3089e52c9d7e57cf43a61e57c1c"
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
    