from enum import StrEnum


class KitchenSinkBulkProfileResponse200OutputDataItemItemCurrentJobType0StartDatePrecisionType1(StrEnum):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
