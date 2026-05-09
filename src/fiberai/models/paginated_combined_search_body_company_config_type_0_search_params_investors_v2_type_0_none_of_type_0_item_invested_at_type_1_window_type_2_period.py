from enum import Enum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsInvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType2Period(
    str, Enum
):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
