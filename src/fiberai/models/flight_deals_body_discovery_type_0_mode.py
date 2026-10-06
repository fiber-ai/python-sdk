from enum import StrEnum


class FlightDealsBodyDiscoveryType0Mode(StrEnum):
    FREETEXT = "freeText"

    def __str__(self) -> str:
        return str(self.value)
