from enum import Enum

class SyncCombinedSearchBodyCompanyParamsLastFundedOnType1WindowType2Period(str, Enum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
