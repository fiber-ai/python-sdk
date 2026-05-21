from enum import Enum


class ProfileLastActivityDateLiveFetchResponse200ChargeInfoType1Method(str, Enum):
    CHARGING_LATER = "charging-later"

    def __str__(self) -> str:
        return str(self.value)
