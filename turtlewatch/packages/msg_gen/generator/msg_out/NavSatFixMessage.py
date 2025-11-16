from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .HeaderMessage import HeaderMessage
from .NavSatStatusMessage import NavSatStatusMessage

@dataclass
class NavSatFixMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    status: NavSatStatusMessage
    latitude: float
    longitude: float
    altitude: float
    position_covariance: list[float]
    COVARIANCE_TYPE_UNKNOWN: int
    COVARIANCE_TYPE_APPROXIMATED: int
    COVARIANCE_TYPE_DIAGONAL_KNOWN: int
    COVARIANCE_TYPE_KNOWN: int
    position_covariance_type: int

    __slots__ = ['header', 'status', 'latitude', 'longitude', 'altitude', 'position_covariance', 'COVARIANCE_TYPE_UNKNOWN', 'COVARIANCE_TYPE_APPROXIMATED', 'COVARIANCE_TYPE_DIAGONAL_KNOWN', 'COVARIANCE_TYPE_KNOWN', 'position_covariance_type']
    _slot_types = ['Header', 'NavSatStatus', 'float64', 'float64', 'float64', 'float64', 'uint8', 'uint8', 'uint8', 'uint8', 'uint8']
    _has_header: bool = False
    _md5sum = "b482668c5fd8868b9b6a29aee579a9c5"
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
    