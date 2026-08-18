from enum import Enum


class FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType3Type1(str, Enum):
    ANNUAL = "annual"
    QUARTERLY = "quarterly"

    def __str__(self) -> str:
        return str(self.value)
