from enum import Enum

class CompanyCountBodySearchParamsJobPostingsV2Type0AnyOfType0ItemPostedAtType1WindowType2Period(str, Enum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
