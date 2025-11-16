from dataclasses import dataclass
from .byteMessage import byteMessage
from .KeyValueMessage import KeyValueMessage

@dataclass
class DiagnosticStatusMessage:
    OK=0: byteMessage
    WARN=1: byteMessage
    ERROR=2: byteMessage
    STALE=3: byteMessage
    level: byteMessage
    name: str
    message: str
    hardware_id: str
    values: list[KeyValueMessage]

    