from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .GoalStatusMessage import GoalStatusMessage
from .HeaderMessage import HeaderMessage

@dataclass
class GoalStatusArrayMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    status_list: list[GoalStatusMessage]

    __slots__ = ['header', 'status_list']
    _slot_types = ['Header', 'GoalStatus']
    _has_header: bool = False
    _md5sum = "c925df0db939d5e1833c7667a01b911c"
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
    