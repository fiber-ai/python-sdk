from enum import StrEnum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsFundingRoundsV2Type0AllOfType0ItemRoundDateType1WindowType0Period(
    StrEnum
):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
