from enum import Enum


class FlightSearchResponse200OutputBestFlightsItemFlightTypeType1(str, Enum):
    MULTI_CITY = "multi_city"
    ONE_WAY = "one_way"
    ROUND_TRIP = "round_trip"

    def __str__(self) -> str:
        return str(self.value)
