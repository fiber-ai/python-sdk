from enum import StrEnum


class FacebookGroupDetailsResponse200ChargeInfoType4Method(StrEnum):
    CREDITS_REFUNDED = "credits-refunded"

    def __str__(self) -> str:
        return str(self.value)
