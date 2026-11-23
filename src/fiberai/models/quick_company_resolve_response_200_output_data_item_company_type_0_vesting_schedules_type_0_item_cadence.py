from enum import StrEnum


class QuickCompanyResolveResponse200OutputDataItemCompanyType0VestingSchedulesType0ItemCadence(StrEnum):
    ANNUALLY = "annually"
    MIXED = "mixed"
    MONTHLY = "monthly"
    OTHER = "other"
    QUARTERLY = "quarterly"
    SEMI_ANNUALLY = "semi-annually"

    def __str__(self) -> str:
        return str(self.value)
