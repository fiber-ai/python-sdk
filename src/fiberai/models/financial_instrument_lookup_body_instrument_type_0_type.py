from enum import StrEnum


class FinancialInstrumentLookupBodyInstrumentType0Type(StrEnum):
    INDEX = "index"

    def __str__(self) -> str:
        return str(self.value)
