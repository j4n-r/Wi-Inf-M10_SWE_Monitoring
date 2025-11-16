from dataclasses import dataclass
from .MapMetaDataMessage import MapMetaDataMessage
from .HeaderMessage import HeaderMessage


@dataclass
class OccupancyGridMessage:
    header: HeaderMessage
    info: MapMetaDataMessage
    data: list[int]
