from dataclasses import dataclass
from typing import Any
import time
from .PoseMessage import PoseMessage
from .ColorRGBAMessage import ColorRGBAMessage
from .PointMessage import PointMessage
from .Vector3Message import Vector3Message
from .HeaderMessage import HeaderMessage

@dataclass
class MarkerMessage:
    header: HeaderMessage
    ns: str
    id: int
    type: int
    action: int
    pose: PoseMessage
    scale: Vector3Message
    color: ColorRGBAMessage
    lifetime: int
    frame_locked: bool
    points: list[PointMessage]
    colors: list[ColorRGBAMessage]
    text: str
    mesh_resource: str
    mesh_use_embedded_materials: bool
    ARROW: int = 0
    CUBE: int = 1
    SPHERE: int = 2
    CYLINDER: int = 3
    LINE_STRIP: int = 4
    LINE_LIST: int = 5
    CUBE_LIST: int = 6
    SPHERE_LIST: int = 7
    POINTS: int = 8
    TEXT_VIEW_FACING: int = 9
    MESH_RESOURCE: int = 10
    TRIANGLE_LIST: int = 11
    ADD: int = 0
    MODIFY: int = 0
    DELETE: int = 2
    DELETEALL: int = 3

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
    