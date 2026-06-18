from enum import Enum


class ListTrackerSignalsFilter(str, Enum):
    ALL = "all"
    DUMMY = "dummy"
    REAL = "real"

    def __str__(self) -> str:
        return str(self.value)
