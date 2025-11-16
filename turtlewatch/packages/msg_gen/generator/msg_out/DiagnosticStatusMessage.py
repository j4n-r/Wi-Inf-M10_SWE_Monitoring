from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .KeyValueMessage import KeyValueMessage

@dataclass
class DiagnosticStatusMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    level: int
    name: str
    message: str
    hardware_id: str
    values: list[KeyValueMessage]
    OK: int = 0
    WARN: int = 1
    ERROR: int = 2
    STALE: int = 3

    __slots__ = ['level', 'name', 'message', 'hardware_id', 'values']
    _slot_types = ['byte', 'byte', 'byte', 'byte', 'byte', 'string', 'string', 'string', 'KeyValue']
    _has_header: bool = False
    _md5sum = "572c9afab4dc9f8be2810aadd26c7eb9"
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
    