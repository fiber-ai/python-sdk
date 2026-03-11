from enum import Enum


class JobPostingSearchResponse200OutputDataItemCompensationRangeType0LteType0Period(str, Enum):
    DAILY = "daily"
    HR = "hr"
    M = "m"
    YR = "yr"

    def __str__(self) -> str:
        return str(self.value)
