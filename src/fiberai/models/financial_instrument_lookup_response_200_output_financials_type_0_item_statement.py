from enum import Enum


class FinancialInstrumentLookupResponse200OutputFinancialsType0ItemStatement(str, Enum):
    BALANCESHEET = "balanceSheet"
    CASHFLOW = "cashFlow"
    INCOMESTATEMENT = "incomeStatement"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
