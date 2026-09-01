from enum import StrEnum


class InstantContactRevealResponse200OutputProfilePhoneNumbersItemTypeType1(StrEnum):
    MOBILE = "mobile"
    OTHER = "other"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
