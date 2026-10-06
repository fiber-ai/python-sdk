from enum import StrEnum


class BookingSearchResponse200ChargeInfoType3Method(StrEnum):
    FREE = "free"

    def __str__(self) -> str:
        return str(self.value)
