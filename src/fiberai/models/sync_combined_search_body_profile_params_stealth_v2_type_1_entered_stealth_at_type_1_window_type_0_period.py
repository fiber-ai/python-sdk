from enum import Enum


class SyncCombinedSearchBodyProfileParamsStealthV2Type1EnteredStealthAtType1WindowType0Period(str, Enum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
