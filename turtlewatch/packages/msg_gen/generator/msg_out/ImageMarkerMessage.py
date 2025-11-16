from dataclasses import dataclass
from typing import Any
import time
from .PointMessage import PointMessage
from .HeaderMessage import HeaderMessage
from .ColorRGBAMessage import ColorRGBAMessage

@dataclass
class ImageMarkerMessage:
    header: HeaderMessage
    ns: str
    id: int
    type: int
    action: int
    position: PointMessage
    scale: float
    outline_color: ColorRGBAMessage
    filled: int
    fill_color: ColorRGBAMessage
    lifetime: int
    points: list[PointMessage]
    outline_colors: list[ColorRGBAMessage]
    CIRCLE: int = 0
    LINE_STRIP: int = 1
    LINE_LIST: int = 2
    POLYGON: int = 3
    POINTS: int = 4
    ADD: int = 0
    REMOVE: int = 1

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
    