from enum import StrEnum


class TenureChangeDirection(StrEnum):
    DECREASED = "decreased"
    INCREASED = "increased"

    def __str__(self) -> str:
        return str(self.value)
