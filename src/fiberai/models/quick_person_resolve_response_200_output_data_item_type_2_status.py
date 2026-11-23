from enum import StrEnum


class QuickPersonResolveResponse200OutputDataItemType2Status(StrEnum):
    OPTED_OUT = "opted_out"

    def __str__(self) -> str:
        return str(self.value)
