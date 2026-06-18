from enum import Enum


class LiteContactRevealResponse200OutputProfilePhoneNumbersItemTypeType1(str, Enum):
    MOBILE = "mobile"
    OTHER = "other"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
