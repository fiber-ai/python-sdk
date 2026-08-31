from enum import StrEnum


class CombinedSearchCountBodyCompanyParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1WindowType2Period(StrEnum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
