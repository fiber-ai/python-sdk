from enum import StrEnum


class FetchRealEstateListingsBodyHomeTypesType0Item(StrEnum):
    APARTMENT = "apartment"
    CONDO = "condo"
    HOUSE = "house"
    LAND = "land"
    MANUFACTURED = "manufactured"
    MULTI_FAMILY = "multi_family"
    TOWNHOUSE = "townhouse"

    def __str__(self) -> str:
        return str(self.value)
