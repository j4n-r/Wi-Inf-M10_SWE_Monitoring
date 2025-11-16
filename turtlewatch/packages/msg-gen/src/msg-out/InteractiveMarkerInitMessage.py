from dataclasses import dataclass
from .InteractiveMarkerMessage import InteractiveMarkerMessage


@dataclass
class InteractiveMarkerInitMessage:
    server_id: str
    seq_num: int
    markers: list[InteractiveMarkerMessage]
