from enum import StrEnum


class BookingSearchBodySortByType3Type1(StrEnum):
    HIGHESTRATING = "highestRating"
    LOWESTPRICE = "lowestPrice"
    MOSTREVIEWED = "mostReviewed"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
