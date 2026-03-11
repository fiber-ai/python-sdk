from enum import Enum


class SyncQuickContactRevealResponse200OutputProfilePhoneNumbersItemType(str, Enum):
    MOBILE = "mobile"
    OTHER = "other"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
