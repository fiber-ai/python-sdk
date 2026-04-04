from enum import Enum


class BuyCreditsResponse200ChargeInfoType3Method(str, Enum):
    FREE = "free"

    def __str__(self) -> str:
        return str(self.value)
