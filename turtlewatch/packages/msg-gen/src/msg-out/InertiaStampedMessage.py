from dataclasses import dataclass
from .HeaderMessage import HeaderMessage
from .InertiaMessage import InertiaMessage


@dataclass
class InertiaStampedMessage:
    header: HeaderMessage
    inertia: InertiaMessage
