from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .Vector3Message import Vector3Message
from .HeaderMessage import HeaderMessage

@dataclass
class MagneticFieldMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    magnetic_field: Vector3Message
    magnetic_field_covariance: list[float]

    __slots__ = ['header', 'magnetic_field', 'magnetic_field_covariance']
    _slot_types = ['Header', 'geometry_msgs/Vector3', 'float64']
    _has_header: bool = False
    _md5sum = "7adfe4dc3f9ad1c89b9423975fbe33dc"
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
    