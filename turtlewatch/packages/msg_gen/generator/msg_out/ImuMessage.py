from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .Vector3Message import Vector3Message
from .QuaternionMessage import QuaternionMessage
from .HeaderMessage import HeaderMessage

@dataclass
class ImuMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    header: HeaderMessage
    orientation: QuaternionMessage
    orientation_covariance: list[float]
    angular_velocity: Vector3Message
    angular_velocity_covariance: list[float]
    linear_acceleration: Vector3Message
    linear_acceleration_covariance: list[float]

    __slots__ = ['header', 'orientation', 'orientation_covariance', 'angular_velocity', 'angular_velocity_covariance', 'linear_acceleration', 'linear_acceleration_covariance']
    _slot_types = ['Header', 'geometry_msgs/Quaternion', 'float64', 'geometry_msgs/Vector3', 'float64', 'geometry_msgs/Vector3', 'float64']
    _has_header: bool = False
    _md5sum = "a6822f3030c123a16dd534c3a913cfc5"
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
    