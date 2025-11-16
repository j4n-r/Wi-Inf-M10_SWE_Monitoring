from dataclasses import dataclass
from .Point32Message import Point32Message


@dataclass
class PolygonMessage:
    points: list[Point32Message]
