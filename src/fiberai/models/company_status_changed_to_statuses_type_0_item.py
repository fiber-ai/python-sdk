from enum import StrEnum


class CompanyStatusChangedToStatusesType0Item(StrEnum):
    ACQUIRED = "acquired"
    CLOSED = "closed"
    IPO = "ipo"
    OPERATING = "operating"
    SUBSIDIARY = "subsidiary"

    def __str__(self) -> str:
        return str(self.value)
