from enum import StrEnum


class FetchRealEstateListingsBodyListingStatusType1(StrEnum):
    FORRENT = "forRent"
    FORSALE = "forSale"
    SOLD = "sold"

    def __str__(self) -> str:
        return str(self.value)
