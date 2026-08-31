from enum import StrEnum


class CompanyCountBodySearchParamsStatusType0AnyOfType0Item(StrEnum):
    ACQUIRED = "acquired"
    ACTIVE = "active"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
