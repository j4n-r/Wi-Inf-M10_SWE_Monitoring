from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .HeaderMessage import HeaderMessage

@dataclass
class ImageMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    height: int
    width: int
    encoding: str
    is_bigendian: int
    step: int
    data: list[int]

    __slots__ = ['header', 'height', 'width', 'encoding', 'is_bigendian', 'step', 'data']
    _slot_types = ['Header', 'uint32', 'uint32', 'string', 'uint8', 'uint32', 'uint8']
    _has_header: bool = False
    _md5sum = "be95f49fd4a2b89351310d45d3d0bda6"
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
    