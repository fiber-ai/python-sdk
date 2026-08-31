from enum import StrEnum


class ResetApiKeyUsageBodyTarget(StrEnum):
    OTHER = "OTHER"
    SELF = "SELF"

    def __str__(self) -> str:
        return str(self.value)
