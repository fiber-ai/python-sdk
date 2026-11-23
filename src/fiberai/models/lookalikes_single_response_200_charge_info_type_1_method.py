from enum import StrEnum


class LookalikesSingleResponse200ChargeInfoType1Method(StrEnum):
    CHARGING_LATER = "charging-later"

    def __str__(self) -> str:
        return str(self.value)
