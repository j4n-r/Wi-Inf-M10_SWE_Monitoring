from dataclasses import dataclass, field
from typing import Any
import genpy
import time

@dataclass
class JoyFeedbackMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    TYPE_LED: int
    TYPE_RUMBLE: int
    TYPE_BUZZER: int
    type: int
    id: int
    intensity: float

    __slots__ = ['TYPE_LED', 'TYPE_RUMBLE', 'TYPE_BUZZER', 'type', 'id', 'intensity']
    _slot_types = ['uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'float32']
    _has_header: bool = False
    _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
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
    