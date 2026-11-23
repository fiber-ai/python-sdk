from enum import StrEnum


class GetBillingHistoryResponse200OutputEntriesItemType0CreditStatusType2Type1(StrEnum):
    CREDITS_GRANTED = "CREDITS_GRANTED"
    FAILED = "FAILED"
    NOT_STARTED = "NOT_STARTED"

    def __str__(self) -> str:
        return str(self.value)
