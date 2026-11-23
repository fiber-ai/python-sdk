from enum import StrEnum


class QuickPersonResolveResponse200OutputDataItemType0PersonType0ExperiencesType0ItemStartDatePrecisionType2Type1(
    StrEnum
):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
