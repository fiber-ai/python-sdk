from enum import StrEnum


class GetTrackerPricingTiersResponse200OutputCompanyListsItemTierType0Tier(StrEnum):
    BASE = "base"
    GOLD = "gold"
    SILVER = "silver"

    def __str__(self) -> str:
        return str(self.value)
