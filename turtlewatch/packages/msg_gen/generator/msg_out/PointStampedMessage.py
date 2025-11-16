from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .PointMessage import PointMessage
from .HeaderMessage import HeaderMessage

@dataclass
class PointStampedMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    point: PointMessage

    __slots__ = ['header', 'point']
    _slot_types = ['Header', 'Point']
    _has_header: bool = False
    _md5sum = "b4fe1b72a19ab2daaedb8b5ba047839b"
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
    