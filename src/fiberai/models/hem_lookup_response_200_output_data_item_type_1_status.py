from enum import StrEnum


class HemLookupResponse200OutputDataItemType1Status(StrEnum):
    NOT_FOUND = "not_found"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
