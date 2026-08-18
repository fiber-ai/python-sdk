from enum import Enum


class FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0PriceChangeType0DirectionType1(str, Enum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
