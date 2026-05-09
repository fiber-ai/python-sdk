from enum import Enum


class FetchRealEstateListingsBodyLocationType1Type(str, Enum):
    STRUCTURED = "structured"

    def __str__(self) -> str:
        return str(self.value)
