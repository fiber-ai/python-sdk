from enum import StrEnum


class FlightSearchBodySortByType2Type1(StrEnum):
    ARRIVALTIME = "arrivalTime"
    DEPARTURETIME = "departureTime"
    DURATION = "duration"
    EMISSIONS = "emissions"
    PRICE = "price"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
