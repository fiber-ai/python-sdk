from enum import StrEnum


class RedditSearchBodyTimeframe(StrEnum):
    ALL = "all"
    DAY = "day"
    MONTH = "month"
    WEEK = "week"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
