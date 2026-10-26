from enum import StrEnum


class KitchenSinkBulkProfileResponse200OutputDataItemItemDetailedWorkExperiencesType0ItemStartDatePrecisionType1(
    StrEnum
):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
