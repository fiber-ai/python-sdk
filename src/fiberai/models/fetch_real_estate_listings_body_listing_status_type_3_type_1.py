from enum import Enum


class FetchRealEstateListingsBodyListingStatusType3Type1(str, Enum):
    FORRENT = "forRent"
    FORSALE = "forSale"
    SOLD = "sold"

    def __str__(self) -> str:
        return str(self.value)
