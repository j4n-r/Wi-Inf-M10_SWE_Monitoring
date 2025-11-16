from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .InteractiveMarkerPoseMessage import InteractiveMarkerPoseMessage
from .InteractiveMarkerMessage import InteractiveMarkerMessage

@dataclass
class InteractiveMarkerUpdateMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    server_id: str
    seq_num: int
    KEEP_ALIVE: int
    UPDATE: int
    type: int
    markers: list[InteractiveMarkerMessage]
    poses: list[InteractiveMarkerPoseMessage]
    erases: list[str]

    __slots__ = ['server_id', 'seq_num', 'KEEP_ALIVE', 'UPDATE', 'type', 'markers', 'poses', 'erases']
    _slot_types = ['string', 'uint64', 'uint8', 'uint8', 'uint8', 'InteractiveMarker', 'InteractiveMarkerPose', 'string']
    _has_header: bool = False
    _md5sum = "710d491a506ef7a835cea53eed4f3cdc"
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
    