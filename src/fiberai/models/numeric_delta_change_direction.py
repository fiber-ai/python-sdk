from enum import Enum


class NumericDeltaChangeDirection(str, Enum):
    DECREASED = "decreased"
    INCREASED = "increased"

    def __str__(self) -> str:
        return str(self.value)
