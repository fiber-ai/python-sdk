from enum import StrEnum


class GetSavedSearchRunProfilesResponse200OutputProfilesItemProfileCurrentJobType0StartDatePrecisionType1(StrEnum):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
