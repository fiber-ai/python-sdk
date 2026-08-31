from enum import StrEnum


class PremiumPhoneRevealResponse200OutputPhoneNumbersItemType(StrEnum):
    MOBILE = "mobile"
    OTHER = "other"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
