from enum import Enum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AllOfType0ItemYearsType0FinishedSchoolAtType1WindowType0Period(
    str, Enum
):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
