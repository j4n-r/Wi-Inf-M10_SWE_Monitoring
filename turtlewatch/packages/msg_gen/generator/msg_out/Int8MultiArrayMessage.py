from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .MultiArrayLayoutMessage import MultiArrayLayoutMessage

@dataclass
class Int8MultiArrayMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    layout: MultiArrayLayoutMessage
    data: list[int]

    __slots__ = ['layout', 'data']
    _slot_types = ['MultiArrayLayout', 'int8']
    _has_header: bool = False
    _md5sum = "925d62b5bfa6994c707ddfac3c012ebb"
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
    