from enum import StrEnum


class SyncBudgetedContactRevealResponse200OutputProfilePhoneNumbersItemType(StrEnum):
    MOBILE = "mobile"
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
