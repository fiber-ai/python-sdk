from enum import StrEnum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobStatusType1LeftAtType1WindowType2Period(StrEnum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
