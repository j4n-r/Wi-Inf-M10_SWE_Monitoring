from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .GoalIDMessage import GoalIDMessage

@dataclass
class GoalStatusMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    goal_id: GoalIDMessage
    status: int
    PENDING: int
    ACTIVE: int
    PREEMPTED: int
    SUCCEEDED: int
    ABORTED: int
    REJECTED: int
    PREEMPTING: int
    RECALLING: int
    RECALLED: int
    LOST: int
    text: str

    __slots__ = ['goal_id', 'status', 'PENDING', 'ACTIVE', 'PREEMPTED', 'SUCCEEDED', 'ABORTED', 'REJECTED', 'PREEMPTING', 'RECALLING', 'RECALLED', 'LOST', 'text']
    _slot_types = ['GoalID', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'string']
    _has_header: bool = False
    _md5sum = "22c3cfa1ecb22bd358e8b6ac088e79a8"
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
    