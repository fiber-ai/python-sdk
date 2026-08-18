from enum import Enum


class FinancialInstrumentLookupBodyInstrumentType4Type(str, Enum):
    CUSTOMSYMBOL = "customSymbol"

    def __str__(self) -> str:
        return str(self.value)
