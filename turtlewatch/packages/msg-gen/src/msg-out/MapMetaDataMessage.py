from dataclasses import dataclass
from .PoseMessage import PoseMessage


@dataclass
class MapMetaDataMessage:
    map_load_time: int
    resolution: float
    width: int
    height: int
    origin: PoseMessage
