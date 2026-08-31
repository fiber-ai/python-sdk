from enum import StrEnum


class CreateSavedSearchBodySearchParamsType1CompanySearchParamsStatusType0AnyOfType0Item(StrEnum):
    ACQUIRED = "acquired"
    ACTIVE = "active"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
