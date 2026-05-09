from enum import Enum


class FetchRealEstateListingsBodyListingStatusType1(str, Enum):
    FORRENT = "forRent"
    FORSALE = "forSale"
    SOLD = "sold"

    def __str__(self) -> str:
        return str(self.value)
