from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .PoseMessage import PoseMessage

@dataclass
class MapMetaDataMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    map_load_time: int
    resolution: float
    width: int
    height: int
    origin: PoseMessage

    __slots__ = ['map_load_time', 'resolution', 'width', 'height', 'origin']
    _slot_types = ['time', 'float32', 'uint32', 'uint32', 'geometry_msgs/Pose']
    _has_header: bool = False
    _md5sum = "545403e3885b890165c1ada675287ee7"
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
    