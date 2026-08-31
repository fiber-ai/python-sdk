from enum import StrEnum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1WindowType0Period(
    StrEnum
):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
