from enum import StrEnum


class QuickPersonResolveResponse200OutputDataItemType1Status(StrEnum):
    NOT_FOUND = "not_found"

    def __str__(self) -> str:
        return str(self.value)
