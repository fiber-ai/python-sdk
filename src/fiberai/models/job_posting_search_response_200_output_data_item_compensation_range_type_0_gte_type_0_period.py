from enum import StrEnum


class JobPostingSearchResponse200OutputDataItemCompensationRangeType0GteType0Period(StrEnum):
    DAILY = "daily"
    HR = "hr"
    M = "m"
    YR = "yr"

    def __str__(self) -> str:
        return str(self.value)
