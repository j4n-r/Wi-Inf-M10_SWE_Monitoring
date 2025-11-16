from dataclasses import dataclass
from .geometry_msgs/PointMessage import geometry_msgs/PointMessage
from .HeaderMessage import HeaderMessage

@dataclass
class GridCellsMessage:
    header: HeaderMessage
    cell_width: float
    cell_height: float
    cells: list[geometry_msgs/PointMessage]

    