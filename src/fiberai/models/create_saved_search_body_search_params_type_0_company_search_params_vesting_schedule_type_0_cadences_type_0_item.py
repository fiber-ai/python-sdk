from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsVestingScheduleType0CadencesType0Item(StrEnum):
    ANNUALLY = "annually"
    MIXED = "mixed"
    MONTHLY = "monthly"
    OTHER = "other"
    QUARTERLY = "quarterly"
    SEMI_ANNUALLY = "semi-annually"

    def __str__(self) -> str:
        return str(self.value)
