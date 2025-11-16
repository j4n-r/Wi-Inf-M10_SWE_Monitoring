from dataclasses import dataclass
from typing import Any
import time
from .HeaderMessage import HeaderMessage
from .PointFieldMessage import PointFieldMessage

@dataclass
class PointCloud2Message:
    header: HeaderMessage
    height: int
    width: int
    fields: list[PointFieldMessage]
    is_bigendian: bool
    point_step: int
    row_step: int
    data: list[int]
    is_dense: bool

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
    