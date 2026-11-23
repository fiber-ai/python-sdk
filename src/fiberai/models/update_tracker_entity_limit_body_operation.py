from enum import StrEnum


class UpdateTrackerEntityLimitBodyOperation(StrEnum):
    DECREASE = "decrease"
    INCREASE = "increase"
    REMOVE = "remove"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
