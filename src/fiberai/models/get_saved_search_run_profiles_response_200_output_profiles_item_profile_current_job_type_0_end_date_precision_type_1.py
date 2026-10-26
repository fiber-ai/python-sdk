from enum import StrEnum


class GetSavedSearchRunProfilesResponse200OutputProfilesItemProfileCurrentJobType0EndDatePrecisionType1(StrEnum):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
