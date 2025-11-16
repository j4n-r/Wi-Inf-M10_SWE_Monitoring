from dataclasses import dataclass
from typing import Any
import time
from .RegionOfInterestMessage import RegionOfInterestMessage
from .ImageMessage import ImageMessage
from .HeaderMessage import HeaderMessage

@dataclass
class DisparityImageMessage:
    header: HeaderMessage
    image: ImageMessage
    f: float
    T: float
    valid_window: RegionOfInterestMessage
    min_disparity: float
    max_disparity: float
    delta_d: float

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
    