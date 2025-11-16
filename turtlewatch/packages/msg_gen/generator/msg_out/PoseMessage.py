from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .PointMessage import PointMessage
from .QuaternionMessage import QuaternionMessage

@dataclass
class PoseMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    position: PointMessage
    orientation: QuaternionMessage

    __slots__ = ['position', 'orientation']
    _slot_types = ['Point', 'Quaternion']
    _has_header: bool = False
    _md5sum = "96cb1222de5c529650d2cc029a955376"
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
    