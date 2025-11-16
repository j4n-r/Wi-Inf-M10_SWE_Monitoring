from dataclasses import dataclass


@dataclass
class JoyFeedbackMessage:
    TYPE_LED: int
    TYPE_RUMBLE: int
    TYPE_BUZZER: int
    type: int
    id: int
    intensity: float
