from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .QuaternionMessage import QuaternionMessage
from .HeaderMessage import HeaderMessage

@dataclass
class QuaternionStampedMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    quaternion: QuaternionMessage

    __slots__ = ['header', 'quaternion']
    _slot_types = ['Header', 'Quaternion']
    _has_header: bool = False
    _md5sum = "cf387d6c8d53742a1d568574ae02d678"
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
    