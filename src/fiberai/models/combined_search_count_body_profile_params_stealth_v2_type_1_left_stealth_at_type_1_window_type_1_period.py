from enum import StrEnum


class CombinedSearchCountBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType1Period(StrEnum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
