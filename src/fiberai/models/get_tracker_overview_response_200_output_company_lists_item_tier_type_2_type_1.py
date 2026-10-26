from enum import StrEnum


class GetTrackerOverviewResponse200OutputCompanyListsItemTierType2Type1(StrEnum):
    BASE = "base"
    GOLD = "gold"
    SILVER = "silver"

    def __str__(self) -> str:
        return str(self.value)
