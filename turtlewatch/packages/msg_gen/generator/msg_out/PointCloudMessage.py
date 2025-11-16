from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .Point32Message import Point32Message
from .ChannelFloat32Message import ChannelFloat32Message
from .HeaderMessage import HeaderMessage

@dataclass
class PointCloudMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    points: list[Point32Message]
    channels: list[ChannelFloat32Message]

    __slots__ = ['header', 'points', 'channels']
    _slot_types = ['Header', 'geometry_msgs/Point32', 'ChannelFloat32']
    _has_header: bool = False
    _md5sum = "56539c60b5ed78c2fc0de075b43ccc2c"
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
    