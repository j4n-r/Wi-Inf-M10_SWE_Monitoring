from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .HeaderMessage import HeaderMessage

@dataclass
class FluidPressureMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    fluid_pressure: float
    variance: float

    __slots__ = ['header', 'fluid_pressure', 'variance']
    _slot_types = ['Header', 'float64', 'float64']
    _has_header: bool = False
    _md5sum = "eb41d088a8c0f20f04e23cc99137c00c"
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
    