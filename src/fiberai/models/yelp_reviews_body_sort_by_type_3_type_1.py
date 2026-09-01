from enum import StrEnum


class YelpReviewsBodySortByType3Type1(StrEnum):
    ELITESFIRST = "elitesFirst"
    HIGHESTRATED = "highestRated"
    LOWESTRATED = "lowestRated"
    NEWESTFIRST = "newestFirst"
    OLDESTFIRST = "oldestFirst"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
