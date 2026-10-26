from enum import StrEnum


class GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemDetailedWorkExperiencesType0ItemEndDatePrecisionType1(
    StrEnum
):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
