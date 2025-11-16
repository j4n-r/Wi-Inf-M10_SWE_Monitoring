from dataclasses import dataclass
from .TwistWithCovarianceMessage import TwistWithCovarianceMessage
from .HeaderMessage import HeaderMessage


@dataclass
class TwistWithCovarianceStampedMessage:
    header: HeaderMessage
    twist: TwistWithCovarianceMessage
