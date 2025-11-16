from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .JoyFeedbackMessage import JoyFeedbackMessage

@dataclass
class JoyFeedbackArrayMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    array: list[JoyFeedbackMessage]

    __slots__ = ['array']
    _slot_types = ['JoyFeedback']
    _has_header: bool = False
    _md5sum = "60f6c486bad093689dd08c556610f7d0"
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
    