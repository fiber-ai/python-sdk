from enum import Enum


class UpdateApiKeyLimitBodyTarget(str, Enum):
    OTHER = "OTHER"
    SELF = "SELF"

    def __str__(self) -> str:
        return str(self.value)
