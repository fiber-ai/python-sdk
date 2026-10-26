from enum import StrEnum


class GetTrackerPricingTiersResponse200OutputPersonListsItemToReachNextTierType1NextTier(StrEnum):
    BASE = "base"
    GOLD = "gold"
    SILVER = "silver"

    def __str__(self) -> str:
        return str(self.value)
