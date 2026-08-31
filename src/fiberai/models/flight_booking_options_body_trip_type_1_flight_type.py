from enum import StrEnum


class FlightBookingOptionsBodyTripType1FlightType(StrEnum):
    ROUND_TRIP = "round_trip"

    def __str__(self) -> str:
        return str(self.value)
