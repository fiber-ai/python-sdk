from enum import Enum


class FinancialInstrumentLookupBodyInstrumentType2Type(str, Enum):
    STOCKORETF = "stockOrEtf"

    def __str__(self) -> str:
        return str(self.value)
