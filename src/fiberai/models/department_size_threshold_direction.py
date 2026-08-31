from enum import StrEnum


class DepartmentSizeThresholdDirection(StrEnum):
    ABOVE = "above"
    BELOW = "below"

    def __str__(self) -> str:
        return str(self.value)
