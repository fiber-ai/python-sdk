from enum import StrEnum


class FinancialInstrumentLookupResponse200OutputExtendedHoursQuoteType0PriceChangeType0DirectionType2Type1(StrEnum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
