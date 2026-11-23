from enum import StrEnum


class UpdateTrackerEntityLimitResponse200ChargeInfoType4Method(StrEnum):
    CREDITS_REFUNDED = "credits-refunded"

    def __str__(self) -> str:
        return str(self.value)
