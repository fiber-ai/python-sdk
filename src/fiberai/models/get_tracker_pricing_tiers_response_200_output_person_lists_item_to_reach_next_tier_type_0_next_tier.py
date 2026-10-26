from enum import StrEnum


class GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType0NextTier(StrEnum):
    BASE = "base"
    GOLD = "gold"
    SILVER = "silver"

    def __str__(self) -> str:
        return str(self.value)
