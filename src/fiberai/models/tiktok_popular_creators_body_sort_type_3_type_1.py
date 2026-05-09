from enum import Enum


class TiktokPopularCreatorsBodySortType3Type1(str, Enum):
    AVERAGE_VIEWS = "average_views"
    ENGAGEMENT = "engagement"
    FOLLOWER = "follower"

    def __str__(self) -> str:
        return str(self.value)
