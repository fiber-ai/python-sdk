from enum import StrEnum


class GetUsageStatsGroupBy(StrEnum):
    APIKEY = "apiKey"
    TOTAL = "total"

    def __str__(self) -> str:
        return str(self.value)
