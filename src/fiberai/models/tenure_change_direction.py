from enum import Enum


class TenureChangeDirection(str, Enum):
    DECREASED = "decreased"
    INCREASED = "increased"

    def __str__(self) -> str:
        return str(self.value)
