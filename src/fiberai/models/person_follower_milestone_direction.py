from enum import StrEnum


class PersonFollowerMilestoneDirection(StrEnum):
    ABOVE = "above"
    BELOW = "below"

    def __str__(self) -> str:
        return str(self.value)
