from enum import StrEnum


class FlightSearchBodyTripType2FlightType(StrEnum):
    MULTI_CITY = "multi_city"

    def __str__(self) -> str:
        return str(self.value)
