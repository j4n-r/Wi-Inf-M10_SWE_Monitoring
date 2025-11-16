from dataclasses import dataclass
from typing import Any
import time
from .InteractiveMarkerControlMessage import InteractiveMarkerControlMessage
from .PoseMessage import PoseMessage
from .MenuEntryMessage import MenuEntryMessage
from .HeaderMessage import HeaderMessage

@dataclass
class InteractiveMarkerMessage:
    header: HeaderMessage
    pose: PoseMessage
    name: str
    description: str
    scale: float
    menu_entries: list[MenuEntryMessage]
    controls: list[InteractiveMarkerControlMessage]

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
    