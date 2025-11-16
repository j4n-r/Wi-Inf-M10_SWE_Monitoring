from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .PointMessage import PointMessage
from .HeaderMessage import HeaderMessage

@dataclass
class GridCellsMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    cell_width: float
    cell_height: float
    cells: list[PointMessage]

    __slots__ = ['header', 'cell_width', 'cell_height', 'cells']
    _slot_types = ['Header', 'float32', 'float32', 'geometry_msgs/Point']
    _has_header: bool = False
    _md5sum = "46b3764d52af7d790149e5be0994fcf9"
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
    