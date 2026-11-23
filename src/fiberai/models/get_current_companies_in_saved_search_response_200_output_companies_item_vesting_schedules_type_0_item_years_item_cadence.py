from enum import StrEnum


class GetCurrentCompaniesInSavedSearchResponse200OutputCompaniesItemVestingSchedulesType0ItemYearsItemCadence(StrEnum):
    ANNUALLY = "annually"
    MONTHLY = "monthly"
    OTHER = "other"
    QUARTERLY = "quarterly"
    SEMI_ANNUALLY = "semi-annually"

    def __str__(self) -> str:
        return str(self.value)
