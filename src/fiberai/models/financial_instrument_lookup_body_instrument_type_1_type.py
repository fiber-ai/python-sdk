from enum import StrEnum


class FinancialInstrumentLookupBodyInstrumentType1Type(StrEnum):
    MUTUALFUND = "mutualFund"

    def __str__(self) -> str:
        return str(self.value)
