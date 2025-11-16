from dataclasses import dataclass


@dataclass
class MeshTriangleMessage:
    vertex_indices: list[int]
