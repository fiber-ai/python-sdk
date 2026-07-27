from enum import Enum


class FlightBookingOptionsBodyTripType0FlightType(str, Enum):
    ONE_WAY = "one_way"

    def __str__(self) -> str:
        return str(self.value)
