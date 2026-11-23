from enum import StrEnum


class LookalikesSingleBodyFiltersType0FundingRoundsV2Type0AnyOfType0ItemRoundDateType1WindowType0Period(StrEnum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
