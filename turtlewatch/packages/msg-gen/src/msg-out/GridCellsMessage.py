from dataclasses import dataclass
from .PointMessage import PointMessage
from .HeaderMessage import HeaderMessage


@dataclass
class GridCellsMessage:
    header: HeaderMessage
    cell_width: float
    cell_height: float
    cells: list[PointMessage]
