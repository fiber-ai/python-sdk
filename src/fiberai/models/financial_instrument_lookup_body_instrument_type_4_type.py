from enum import StrEnum


class FinancialInstrumentLookupBodyInstrumentType4Type(StrEnum):
    CUSTOMSYMBOL = "customSymbol"

    def __str__(self) -> str:
        return str(self.value)
