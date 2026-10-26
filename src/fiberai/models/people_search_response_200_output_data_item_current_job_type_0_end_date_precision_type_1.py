from enum import StrEnum


class PeopleSearchResponse200OutputDataItemCurrentJobType0EndDatePrecisionType1(StrEnum):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
