from enum import StrEnum


class GetSavedSearchRunProfilesResponse200OutputProfilesItemProfileExperiencesType0ItemStartDatePrecisionType1(StrEnum):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
