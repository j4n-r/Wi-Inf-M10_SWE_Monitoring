from dataclasses import dataclass
from .AccelWithCovarianceMessage import AccelWithCovarianceMessage
from .HeaderMessage import HeaderMessage


@dataclass
class AccelWithCovarianceStampedMessage:
    header: HeaderMessage
    accel: AccelWithCovarianceMessage
