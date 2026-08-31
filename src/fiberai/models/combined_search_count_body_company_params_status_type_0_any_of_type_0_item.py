from enum import StrEnum


class CombinedSearchCountBodyCompanyParamsStatusType0AnyOfType0Item(StrEnum):
    ACQUIRED = "acquired"
    ACTIVE = "active"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
