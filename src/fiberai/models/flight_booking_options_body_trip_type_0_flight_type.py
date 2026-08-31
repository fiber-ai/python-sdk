from enum import StrEnum


class FlightBookingOptionsBodyTripType0FlightType(StrEnum):
    ONE_WAY = "one_way"

    def __str__(self) -> str:
        return str(self.value)
