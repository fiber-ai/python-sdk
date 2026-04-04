from enum import Enum


class CompanySearchBodySearchParamsInvestorsV2Type0AllOfType0ItemInvestedAtType1WindowType1Period(str, Enum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
