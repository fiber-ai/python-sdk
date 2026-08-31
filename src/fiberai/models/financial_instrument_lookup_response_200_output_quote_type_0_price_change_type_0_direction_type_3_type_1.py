from enum import StrEnum


class FinancialInstrumentLookupResponse200OutputQuoteType0PriceChangeType0DirectionType3Type1(StrEnum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
