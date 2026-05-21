from enum import Enum


class UpdateJobChangeListResponse200ChargeInfoType4Method(str, Enum):
    CREDITS_REFUNDED = "credits-refunded"

    def __str__(self) -> str:
        return str(self.value)
