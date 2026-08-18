from enum import Enum


class UpdateApiKeyExpirationBodyTarget(str, Enum):
    OTHER = "OTHER"
    SELF = "SELF"

    def __str__(self) -> str:
        return str(self.value)
