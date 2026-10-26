from enum import StrEnum


class QuickPersonResolveResponse200OutputDataItemPersonType0DetailedWorkExperiencesType0ItemEndDatePrecisionType1(
    StrEnum
):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
