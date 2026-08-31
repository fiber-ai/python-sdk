from enum import StrEnum


class RevokeCurrentApiKeyBodyTarget(StrEnum):
    OTHER = "OTHER"
    SELF = "SELF"

    def __str__(self) -> str:
        return str(self.value)
