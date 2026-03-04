from enum import Enum

class CombinedSearchBodyProfileParamsStealthV2Type1LeftStealthAtType1WindowType2Period(str, Enum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
