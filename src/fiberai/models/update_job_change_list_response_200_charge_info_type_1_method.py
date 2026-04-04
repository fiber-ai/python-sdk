from enum import Enum


class UpdateJobChangeListResponse200ChargeInfoType1Method(str, Enum):
    CHARGING_LATER = "charging-later"

    def __str__(self) -> str:
        return str(self.value)
