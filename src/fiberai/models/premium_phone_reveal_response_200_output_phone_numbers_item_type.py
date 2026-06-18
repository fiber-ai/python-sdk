from enum import Enum


class PremiumPhoneRevealResponse200OutputPhoneNumbersItemType(str, Enum):
    MOBILE = "mobile"
    OTHER = "other"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
