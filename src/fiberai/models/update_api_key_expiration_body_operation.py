from enum import Enum


class UpdateApiKeyExpirationBodyOperation(str, Enum):
    EXTEND = "extend"
    PREPONE = "prepone"
    REMOVE = "remove"
    SET = "set"

    def __str__(self) -> str:
        return str(self.value)
