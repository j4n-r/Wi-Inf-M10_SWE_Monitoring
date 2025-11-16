from dataclasses import dataclass
from typing import Any
import time
from .RegionOfInterestMessage import RegionOfInterestMessage
from .HeaderMessage import HeaderMessage

@dataclass
class CameraInfoMessage:
    header: HeaderMessage
    height: int
    width: int
    distortion_model: str
    D: list[float]
    K: list[float]
    R: list[float]
    P: list[float]
    binning_x: int
    binning_y: int
    roi: RegionOfInterestMessage

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
    