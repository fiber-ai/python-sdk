from enum import StrEnum


class GetBillingHistoryResponse200OutputEntriesItemType0PurchaseType(StrEnum):
    AUTOTOPUP = "autoTopup"
    SUBSCRIPTION = "subscription"
    TOPUP = "topup"

    def __str__(self) -> str:
        return str(self.value)
