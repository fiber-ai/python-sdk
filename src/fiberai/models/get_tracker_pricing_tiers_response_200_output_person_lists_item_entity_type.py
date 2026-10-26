from enum import StrEnum


class GetTrackerPricingTiersResponse200OutputPersonListsItemEntityType(StrEnum):
    COMPANY = "company"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
