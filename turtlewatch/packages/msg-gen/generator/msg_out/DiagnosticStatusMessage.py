from dataclasses import dataclass
from typing import Any
import time
from .KeyValueMessage import KeyValueMessage

@dataclass
class DiagnosticStatusMessage:
    level: int
    name: str
    message: str
    hardware_id: str
    values: list[KeyValueMessage]
    OK: int = 0
    WARN: int = 1
    ERROR: int = 2
    STALE: int = 3

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
    