from dataclasses import dataclass
from .JoyFeedbackMessage import JoyFeedbackMessage


@dataclass
class JoyFeedbackArrayMessage:
    array: list[JoyFeedbackMessage]
