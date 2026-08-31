from enum import StrEnum


class FetchRealEstateListingsBodySortByType2Type1(StrEnum):
    BATHROOMCOUNTDESCENDING = "bathroomCountDescending"
    BEDROOMCOUNTDESCENDING = "bedroomCountDescending"
    ESTIMATEDPRICEASCENDING = "estimatedPriceAscending"
    ESTIMATEDPRICEDESCENDING = "estimatedPriceDescending"
    FLOORAREASQFTDESCENDING = "floorAreaSqFtDescending"
    LOTAREASQFTDESCENDING = "lotAreaSqFtDescending"
    NEWEST = "newest"
    PAYMENTASCENDING = "paymentAscending"
    PAYMENTDESCENDING = "paymentDescending"
    PRICEASCENDING = "priceAscending"
    PRICEDESCENDING = "priceDescending"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
