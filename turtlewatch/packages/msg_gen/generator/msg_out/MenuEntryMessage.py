from dataclasses import dataclass, field
from typing import Any
import genpy
import time

@dataclass
class MenuEntryMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    id: int
    parent_id: int
    title: str
    command: str
    command_type: int
    FEEDBACK: int = 0
    ROSRUN: int = 1
    ROSLAUNCH: int = 2

    __slots__ = ['id', 'parent_id', 'title', 'command', 'command_type']
    _slot_types = ['uint32', 'uint32', 'string', 'string', 'uint8', 'uint8', 'uint8', 'uint8']
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
    