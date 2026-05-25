from enum import Enum


class CompanyStatusChangedToStatusesType0Item(str, Enum):
    ACQUIRED = "acquired"
    CLOSED = "closed"
    IPO = "ipo"
    OPERATING = "operating"
    SUBSIDIARY = "subsidiary"

    def __str__(self) -> str:
        return str(self.value)
