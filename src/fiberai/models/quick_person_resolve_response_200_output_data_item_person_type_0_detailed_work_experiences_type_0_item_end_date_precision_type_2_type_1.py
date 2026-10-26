from enum import StrEnum


class QuickPersonResolveResponse200OutputDataItemPersonType0DetailedWorkExperiencesType0ItemEndDatePrecisionType2Type1(
    StrEnum
):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
