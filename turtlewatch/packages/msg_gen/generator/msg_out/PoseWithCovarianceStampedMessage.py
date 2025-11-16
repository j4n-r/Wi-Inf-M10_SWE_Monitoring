from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .PoseWithCovarianceMessage import PoseWithCovarianceMessage
from .HeaderMessage import HeaderMessage

@dataclass
class PoseWithCovarianceStampedMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    pose: PoseWithCovarianceMessage

    __slots__ = ['header', 'pose']
    _slot_types = ['Header', 'PoseWithCovariance']
    _has_header: bool = False
    _md5sum = "6fb5f17c5243462be64c84d954db30b4"
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
    