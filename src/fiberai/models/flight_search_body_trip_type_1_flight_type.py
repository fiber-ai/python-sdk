from enum import Enum


class FlightSearchBodyTripType1FlightType(str, Enum):
    ROUND_TRIP = "round_trip"

    def __str__(self) -> str:
        return str(self.value)
