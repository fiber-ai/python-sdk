from enum import Enum


class FlightBookingOptionsBodyTripType2FlightType(str, Enum):
    MULTI_CITY = "multi_city"

    def __str__(self) -> str:
        return str(self.value)
