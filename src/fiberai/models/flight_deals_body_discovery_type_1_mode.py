from enum import StrEnum


class FlightDealsBodyDiscoveryType1Mode(StrEnum):
    FILTERS = "filters"

    def __str__(self) -> str:
        return str(self.value)
