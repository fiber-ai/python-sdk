from enum import Enum


class FlightSearchBodySortByType2Type1(str, Enum):
    ARRIVALTIME = "arrivalTime"
    DEPARTURETIME = "departureTime"
    DURATION = "duration"
    EMISSIONS = "emissions"
    PRICE = "price"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
