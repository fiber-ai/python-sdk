from enum import StrEnum


class CombinedSearchCountBodyProfileParamsStealthV2Type1EnteredStealthAtType1WindowType2Period(StrEnum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
