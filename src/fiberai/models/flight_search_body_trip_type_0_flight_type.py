from enum import Enum


class FlightSearchBodyTripType0FlightType(str, Enum):
    ONE_WAY = "one_way"

    def __str__(self) -> str:
        return str(self.value)
