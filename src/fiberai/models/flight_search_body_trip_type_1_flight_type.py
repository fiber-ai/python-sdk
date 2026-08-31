from enum import StrEnum


class FlightSearchBodyTripType1FlightType(StrEnum):
    ROUND_TRIP = "round_trip"

    def __str__(self) -> str:
        return str(self.value)
