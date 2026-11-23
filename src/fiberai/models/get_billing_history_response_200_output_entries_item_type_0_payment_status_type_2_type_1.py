from enum import StrEnum


class GetBillingHistoryResponse200OutputEntriesItemType0PaymentStatusType2Type1(StrEnum):
    NOT_STARTED = "NOT_STARTED"
    PAID = "PAID"

    def __str__(self) -> str:
        return str(self.value)
