from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsInvestorsV2Type0NoneOfType0ItemInvestedAtType1WindowType0Period(
    StrEnum
):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
