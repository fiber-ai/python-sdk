from enum import StrEnum


class UpdateApiKeyLimitBodyTarget(StrEnum):
    OTHER = "OTHER"
    SELF = "SELF"

    def __str__(self) -> str:
        return str(self.value)
