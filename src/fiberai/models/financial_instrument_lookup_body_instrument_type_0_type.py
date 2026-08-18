from enum import Enum


class FinancialInstrumentLookupBodyInstrumentType0Type(str, Enum):
    INDEX = "index"

    def __str__(self) -> str:
        return str(self.value)
