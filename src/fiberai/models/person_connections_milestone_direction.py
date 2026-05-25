from enum import Enum


class PersonConnectionsMilestoneDirection(str, Enum):
    ABOVE = "above"
    BELOW = "below"

    def __str__(self) -> str:
        return str(self.value)
