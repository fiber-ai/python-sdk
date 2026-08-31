from enum import StrEnum


class FinancialInstrumentLookupResponse200OutputFinancialsType0ItemPeriodsType0ItemPeriodTypeType3Type1(StrEnum):
    ANNUAL = "annual"
    QUARTERLY = "quarterly"

    def __str__(self) -> str:
        return str(self.value)
