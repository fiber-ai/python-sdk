from enum import StrEnum


class GetCurrentApiKeyBodyTarget(StrEnum):
    OTHER = "OTHER"
    SELF = "SELF"

    def __str__(self) -> str:
        return str(self.value)
