from enum import Enum

class TextToProfileSearchResponse200OutputSearchParamsEducationType0AnyOfType0ItemStartedSchoolAtType1WindowType0Period(str, Enum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
