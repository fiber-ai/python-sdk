from enum import StrEnum


class UpdateApiKeyLimitBodyWindow(StrEnum):
    DAY = "day"
    LIFETIME = "lifetime"
    WEEK = "week"

    def __str__(self) -> str:
        return str(self.value)
