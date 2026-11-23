from enum import StrEnum


class PaginatedCombinedSearchResponse200OutputCompaniesItemVestingSchedulesType0ItemCadence(StrEnum):
    ANNUALLY = "annually"
    MIXED = "mixed"
    MONTHLY = "monthly"
    OTHER = "other"
    QUARTERLY = "quarterly"
    SEMI_ANNUALLY = "semi-annually"

    def __str__(self) -> str:
        return str(self.value)
