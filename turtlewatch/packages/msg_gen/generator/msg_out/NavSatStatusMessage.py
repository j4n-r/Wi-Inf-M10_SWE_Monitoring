from dataclasses import dataclass, field
from typing import Any
import genpy
import time

@dataclass
class NavSatStatusMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    STATUS_NO_FIX: int
    STATUS_FIX: int
    STATUS_SBAS_FIX: int
    STATUS_GBAS_FIX: int
    status: int
    SERVICE_GPS: int
    SERVICE_GLONASS: int
    SERVICE_COMPASS: int
    SERVICE_GALILEO: int
    service: int

    __slots__ = ['STATUS_NO_FIX', 'STATUS_FIX', 'STATUS_SBAS_FIX', 'STATUS_GBAS_FIX', 'status', 'SERVICE_GPS', 'SERVICE_GLONASS', 'SERVICE_COMPASS', 'SERVICE_GALILEO', 'service']
    _slot_types = ['int8', 'int8', 'int8', 'int8', 'int8', 'uint16', 'uint16', 'uint16', 'uint16', 'uint16']
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
    