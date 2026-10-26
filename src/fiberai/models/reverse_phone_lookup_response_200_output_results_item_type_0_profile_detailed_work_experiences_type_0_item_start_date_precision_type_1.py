from enum import StrEnum


class ReversePhoneLookupResponse200OutputResultsItemType0ProfileDetailedWorkExperiencesType0ItemStartDatePrecisionType1(
    StrEnum
):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
