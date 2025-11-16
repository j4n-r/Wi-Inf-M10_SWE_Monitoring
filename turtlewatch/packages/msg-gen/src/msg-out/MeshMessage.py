from dataclasses import dataclass
from .MeshTriangleMessage import MeshTriangleMessage
from .geometry_msgs/PointMessage import geometry_msgs/PointMessage

@dataclass
class MeshMessage:
    triangles: list[MeshTriangleMessage]
    vertices: list[geometry_msgs/PointMessage]

    