from dataclasses import dataclass, field
from typing import Any
import genpy
import time
from .TwistMessage import TwistMessage
from .TransformMessage import TransformMessage

@dataclass
class MultiDOFJointTrajectoryPointMessage(genpy.Message):
    _type: str # topic type \cmd_vel
    transforms: list[TransformMessage]
    velocities: list[TwistMessage]
    accelerations: list[TwistMessage]
    time_from_start: int

    __slots__ = ['transforms', 'velocities', 'accelerations', 'time_from_start']
    _slot_types = ['geometry_msgs/Transform', 'geometry_msgs/Twist', 'geometry_msgs/Twist', 'duration']
    _has_header: bool = False
    _md5sum = "8a936f7d08b80f0f05b210858e87ffe2"
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
    