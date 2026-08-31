from enum import StrEnum


class UpdateApiKeyExpirationBodyTarget(StrEnum):
    OTHER = "OTHER"
    SELF = "SELF"

    def __str__(self) -> str:
        return str(self.value)
