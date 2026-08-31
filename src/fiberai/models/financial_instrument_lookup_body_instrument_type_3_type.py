from enum import StrEnum


class FinancialInstrumentLookupBodyInstrumentType3Type(StrEnum):
    CURRENCYPAIR = "currencyPair"

    def __str__(self) -> str:
        return str(self.value)
