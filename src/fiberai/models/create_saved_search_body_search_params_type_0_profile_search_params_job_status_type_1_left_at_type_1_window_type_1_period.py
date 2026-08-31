from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobStatusType1LeftAtType1WindowType1Period(StrEnum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
