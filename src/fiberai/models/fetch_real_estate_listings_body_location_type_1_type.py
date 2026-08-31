from enum import StrEnum


class FetchRealEstateListingsBodyLocationType1Type(StrEnum):
    STRUCTURED = "structured"

    def __str__(self) -> str:
        return str(self.value)
