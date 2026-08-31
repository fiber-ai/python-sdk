from enum import StrEnum


class FlightBookingOptionsBodyTripType2FlightType(StrEnum):
    MULTI_CITY = "multi_city"

    def __str__(self) -> str:
        return str(self.value)
