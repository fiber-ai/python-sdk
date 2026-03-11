from enum import Enum


class CombinedSearchBodyCompanyParamsStatusType0NoneOfType0Item(str, Enum):
    ACQUIRED = "acquired"
    ACTIVE = "active"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
