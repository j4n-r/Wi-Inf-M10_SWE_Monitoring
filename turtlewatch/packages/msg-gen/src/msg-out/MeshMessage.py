from dataclasses import dataclass
from .PointMessage import PointMessage
from .MeshTriangleMessage import MeshTriangleMessage


@dataclass
class MeshMessage:
    triangles: list[MeshTriangleMessage]
    vertices: list[PointMessage]
