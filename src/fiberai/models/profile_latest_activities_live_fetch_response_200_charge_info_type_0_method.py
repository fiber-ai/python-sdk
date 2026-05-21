from enum import Enum


class ProfileLatestActivitiesLiveFetchResponse200ChargeInfoType0Method(str, Enum):
    CHARGED_NOW = "charged-now"

    def __str__(self) -> str:
        return str(self.value)
