from enum import StrEnum


class GetCurrentProfilesInSavedSearchResponse200OutputProfilesItemCurrentJobType0EndDatePrecisionType1(StrEnum):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
