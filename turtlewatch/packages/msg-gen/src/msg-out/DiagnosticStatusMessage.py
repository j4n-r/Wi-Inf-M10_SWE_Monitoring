from dataclasses import dataclass
from .KeyValueMessage import KeyValueMessage


@dataclass
class DiagnosticStatusMessage:
    level: int
    name: str
    message: str
    hardware_id: str
    values: list[KeyValueMessage]
    OK: int = 0
    WARN: int = 1
    ERROR: int = 2
    STALE: int = 3
