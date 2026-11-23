from enum import StrEnum


class GetBillingHistoryResponse200OutputEntriesItemType1PaymentStatus(StrEnum):
    FAILED = "FAILED"

    def __str__(self) -> str:
        return str(self.value)
