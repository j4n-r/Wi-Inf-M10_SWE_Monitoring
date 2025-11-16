from dataclasses import dataclass
from .GoalStatusMessage import GoalStatusMessage
from .HeaderMessage import HeaderMessage


@dataclass
class GoalStatusArrayMessage:
    header: HeaderMessage
    status_list: list[GoalStatusMessage]
