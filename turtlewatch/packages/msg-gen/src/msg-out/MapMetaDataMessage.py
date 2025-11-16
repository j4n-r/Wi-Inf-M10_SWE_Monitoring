from dataclasses import dataclass
from .geometry_msgs/PoseMessage import geometry_msgs/PoseMessage

@dataclass
class MapMetaDataMessage:
    map_load_time: int
    resolution: float
    width: int
    height: int
    origin: geometry_msgs/PoseMessage

    