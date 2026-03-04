from enum import Enum

class TextToCompanySearchParamsResponse200OutputSearchParamsJobPostingsV2Type0NoneOfType0ItemPostedAtType1WindowType1Period(str, Enum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
