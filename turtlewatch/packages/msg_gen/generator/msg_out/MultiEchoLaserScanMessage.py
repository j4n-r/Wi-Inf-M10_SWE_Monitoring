from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .LaserEchoMessage import LaserEchoMessage
from .HeaderMessage import HeaderMessage

@dataclass
class MultiEchoLaserScanMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    angle_min: float
    angle_max: float
    angle_increment: float
    time_increment: float
    scan_time: float
    range_min: float
    range_max: float
    ranges: list[LaserEchoMessage]
    intensities: list[LaserEchoMessage]

    __slots__ = ['header', 'angle_min', 'angle_max', 'angle_increment', 'time_increment', 'scan_time', 'range_min', 'range_max', 'ranges', 'intensities']
    _slot_types = ['Header', 'float32', 'float32', 'float32', 'float32', 'float32', 'float32', 'float32', 'LaserEcho', 'LaserEcho']
    _has_header: bool = False
    _md5sum = "c396f044c85be204606aa5e15fd4fbe6"
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
    