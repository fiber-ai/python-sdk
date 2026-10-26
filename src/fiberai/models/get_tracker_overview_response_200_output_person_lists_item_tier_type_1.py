from enum import StrEnum


class GetTrackerOverviewResponse200OutputPersonListsItemTierType1(StrEnum):
    BASE = "base"
    GOLD = "gold"
    SILVER = "silver"

    def __str__(self) -> str:
        return str(self.value)
