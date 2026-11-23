from enum import StrEnum


class GetUsageStatsGranularity(StrEnum):
    ALL = "all"
    DAY = "day"
    HOUR = "hour"
    MINUTE = "minute"
    MONTH = "month"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
