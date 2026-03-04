from enum import Enum

class PeopleSearchCountBodySearchParamsStealthV2Type0EnteredStealthAtType1WindowType0Period(str, Enum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
