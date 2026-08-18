from enum import Enum


class FinancialInstrumentLookupBodyInstrumentType1Type(str, Enum):
    MUTUALFUND = "mutualFund"

    def __str__(self) -> str:
        return str(self.value)
