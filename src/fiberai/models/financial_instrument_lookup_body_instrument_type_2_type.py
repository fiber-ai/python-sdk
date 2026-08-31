from enum import StrEnum


class FinancialInstrumentLookupBodyInstrumentType2Type(StrEnum):
    STOCKORETF = "stockOrEtf"

    def __str__(self) -> str:
        return str(self.value)
