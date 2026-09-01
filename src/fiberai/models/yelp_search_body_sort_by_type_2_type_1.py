from enum import StrEnum


class YelpSearchBodySortByType2Type1(StrEnum):
    HIGHESTRATED = "highestRated"
    MOSTREVIEWED = "mostReviewed"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
