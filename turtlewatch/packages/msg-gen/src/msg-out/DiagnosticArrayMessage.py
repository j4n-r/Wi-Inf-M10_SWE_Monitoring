from dataclasses import dataclass
from .DiagnosticStatusMessage import DiagnosticStatusMessage
from .HeaderMessage import HeaderMessage


@dataclass
class DiagnosticArrayMessage:
    header: HeaderMessage
    status: list[DiagnosticStatusMessage]
