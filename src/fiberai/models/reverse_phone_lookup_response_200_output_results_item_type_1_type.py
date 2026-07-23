from enum import Enum


class ReversePhoneLookupResponse200OutputResultsItemType1Type(str, Enum):
    COMPANY = "company"

    def __str__(self) -> str:
        return str(self.value)
