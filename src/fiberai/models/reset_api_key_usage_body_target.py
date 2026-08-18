from enum import Enum


class ResetApiKeyUsageBodyTarget(str, Enum):
    OTHER = "OTHER"
    SELF = "SELF"

    def __str__(self) -> str:
        return str(self.value)
