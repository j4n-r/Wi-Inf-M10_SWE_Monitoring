from dataclasses import dataclass
from .GoalIDMessage import GoalIDMessage


@dataclass
class GoalStatusMessage:
    goal_id: GoalIDMessage
    status: int
    PENDING: int
    ACTIVE: int
    PREEMPTED: int
    SUCCEEDED: int
    ABORTED: int
    REJECTED: int
    PREEMPTING: int
    RECALLING: int
    RECALLED: int
    LOST: int
    text: str
