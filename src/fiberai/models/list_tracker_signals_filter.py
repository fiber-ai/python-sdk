from enum import StrEnum


class ListTrackerSignalsFilter(StrEnum):
    ALL = "all"
    DUMMY = "dummy"
    REAL = "real"

    def __str__(self) -> str:
        return str(self.value)
