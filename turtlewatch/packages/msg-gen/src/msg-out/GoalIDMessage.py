from dataclasses import dataclass


@dataclass
class GoalIDMessage:
    stamp: int
    id: str
