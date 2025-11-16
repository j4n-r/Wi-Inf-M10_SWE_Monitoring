from dataclasses import dataclass, field
from typing import Any
import genpy
import time

@dataclass
class SolidPrimitiveMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    type: int
    dimensions: list[float]
    BOX: int = 1
    SPHERE: int = 2
    CYLINDER: int = 3
    CONE: int = 4
    BOX_X: int = 0
    BOX_Y: int = 1
    BOX_Z: int = 2
    SPHERE_RADIUS: int = 0
    CYLINDER_HEIGHT: int = 0
    CYLINDER_RADIUS: int = 1
    CONE_HEIGHT: int = 0
    CONE_RADIUS: int = 1

    __slots__ = ['type', 'dimensions']
    _slot_types = ['uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'float64', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8']
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
    