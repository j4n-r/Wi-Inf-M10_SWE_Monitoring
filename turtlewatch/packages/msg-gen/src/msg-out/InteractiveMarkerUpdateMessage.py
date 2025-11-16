from dataclasses import dataclass
from .InteractiveMarkerPoseMessage import InteractiveMarkerPoseMessage
from .InteractiveMarkerMessage import InteractiveMarkerMessage


@dataclass
class InteractiveMarkerUpdateMessage:
    server_id: str
    seq_num: int
    KEEP_ALIVE: int
    UPDATE: int
    type: int
    markers: list[InteractiveMarkerMessage]
    poses: list[InteractiveMarkerPoseMessage]
    erases: list[str]
