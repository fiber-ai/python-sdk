from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsInvestorsV2Type0AnyOfType0ItemInvestedAtType1WindowType2Period(
    StrEnum
):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
