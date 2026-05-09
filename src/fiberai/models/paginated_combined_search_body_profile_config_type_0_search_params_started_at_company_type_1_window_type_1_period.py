from enum import Enum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsStartedAtCompanyType1WindowType1Period(str, Enum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
