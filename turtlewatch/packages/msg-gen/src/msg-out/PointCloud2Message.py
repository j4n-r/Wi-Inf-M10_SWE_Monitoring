from dataclasses import dataclass
from .HeaderMessage import HeaderMessage
from .PointFieldMessage import PointFieldMessage


@dataclass
class PointCloud2Message:
    header: HeaderMessage
    height: int
    width: int
    fields: list[PointFieldMessage]
    is_bigendian: bool
    point_step: int
    row_step: int
    data: list[int]
    is_dense: bool
