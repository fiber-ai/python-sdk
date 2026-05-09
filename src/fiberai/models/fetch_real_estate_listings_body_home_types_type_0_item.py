from enum import Enum


class FetchRealEstateListingsBodyHomeTypesType0Item(str, Enum):
    APARTMENT = "apartment"
    CONDO = "condo"
    HOUSE = "house"
    LAND = "land"
    MANUFACTURED = "manufactured"
    MULTI_FAMILY = "multi_family"
    TOWNHOUSE = "townhouse"

    def __str__(self) -> str:
        return str(self.value)
