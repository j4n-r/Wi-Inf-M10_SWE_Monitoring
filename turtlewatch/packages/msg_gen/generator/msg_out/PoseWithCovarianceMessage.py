from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .PoseMessage import PoseMessage

@dataclass
class PoseWithCovarianceMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    pose: PoseMessage
    covariance: list[float]

    __slots__ = ['pose', 'covariance']
    _slot_types = ['Pose', 'float64']
    _has_header: bool = False
    _md5sum = "3f91634a80b7f6d79b12232c57189e9e"
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
    