from enum import StrEnum


class QuickPersonResolveResponse200OutputDataItemPersonType0CurrentJobType0EndDatePrecisionType1(StrEnum):
    MONTH = "month"
    YEAR = "year"

    def __str__(self) -> str:
        return str(self.value)
