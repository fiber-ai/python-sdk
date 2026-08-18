from enum import Enum


class FinancialInstrumentLookupBodyInstrumentType3Type(str, Enum):
    CURRENCYPAIR = "currencyPair"

    def __str__(self) -> str:
        return str(self.value)
