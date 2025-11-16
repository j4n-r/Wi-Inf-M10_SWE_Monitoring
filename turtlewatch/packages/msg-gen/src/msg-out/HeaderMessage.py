from dataclasses import dataclass


@dataclass
class HeaderMessage:
    seq: int
    stamp: int
    frame_id: str
