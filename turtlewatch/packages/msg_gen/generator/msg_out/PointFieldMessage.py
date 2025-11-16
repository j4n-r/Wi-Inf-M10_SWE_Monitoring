from dataclasses import dataclass, field
from typing import Any
import genpy
import time

@dataclass
class PointFieldMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    INT8: int
    UINT8: int
    INT16: int
    UINT16: int
    INT32: int
    UINT32: int
    FLOAT32: int
    FLOAT64: int
    name: str
    offset: int
    datatype: int
    count: int

    __slots__ = ['INT8', 'UINT8', 'INT16', 'UINT16', 'INT32', 'UINT32', 'FLOAT32', 'FLOAT64', 'name', 'offset', 'datatype', 'count']
    _slot_types = ['uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8', 'string', 'uint32', 'uint8', 'uint32']
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
    