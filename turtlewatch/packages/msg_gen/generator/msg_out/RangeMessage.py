from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .HeaderMessage import HeaderMessage

@dataclass
class RangeMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    radiation_type: int
    field_of_view: float
    min_range: float
    max_range: float
    range: float
    ULTRASOUND: int = 0
    INFRARED: int = 1

    __slots__ = ['header', 'radiation_type', 'field_of_view', 'min_range', 'max_range', 'range']
    _slot_types = ['Header', 'uint8', 'uint8', 'uint8', 'float32', 'float32', 'float32', 'float32']
    _has_header: bool = False
    _md5sum = "712e00f0cd3e221fb2b25d2a983bd223"
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
    