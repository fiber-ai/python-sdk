from enum import Enum


class TextToCombinedSearchResponse200OutputProfileSearchParamsType0EducationType0AnyOfType0ItemFinishedSchoolAtType1WindowType1Period(
    str, Enum
):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
