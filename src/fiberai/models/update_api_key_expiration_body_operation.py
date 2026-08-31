from enum import StrEnum


class UpdateApiKeyExpirationBodyOperation(StrEnum):
    EXTEND = "extend"
    PREPONE = "prepone"
    REMOVE = "remove"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
