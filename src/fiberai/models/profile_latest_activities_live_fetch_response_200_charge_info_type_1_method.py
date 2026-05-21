from enum import Enum


class ProfileLatestActivitiesLiveFetchResponse200ChargeInfoType1Method(str, Enum):
    CHARGING_LATER = "charging-later"

    def __str__(self) -> str:
        return str(self.value)
