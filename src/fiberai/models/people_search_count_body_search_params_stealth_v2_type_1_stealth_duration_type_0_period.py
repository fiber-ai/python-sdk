from enum import StrEnum


class PeopleSearchCountBodySearchParamsStealthV2Type1StealthDurationType0Period(StrEnum):
    DAY = "day"
    MONTH = "month"
    QUARTER = "quarter"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
