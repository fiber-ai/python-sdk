from enum import StrEnum


class GetBillingHistoryResponse200OutputEntriesItemType1PurchaseType(StrEnum):
    AUTOTOPUP = "autoTopup"
    TOPUP = "topup"

    def __str__(self) -> str:
        return str(self.value)
