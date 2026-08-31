from enum import StrEnum


class FinancialInstrumentLookupResponse200OutputFinancialsType0ItemStatement(StrEnum):
    BALANCESHEET = "balanceSheet"
    CASHFLOW = "cashFlow"
    INCOMESTATEMENT = "incomeStatement"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
