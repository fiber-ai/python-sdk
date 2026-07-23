from enum import Enum


class HotelSearchResponse200OutputPropertiesItemTypeType2Type1(str, Enum):
    HOTEL = "hotel"
    VACATIONRENTAL = "vacationRental"

    def __str__(self) -> str:
        return str(self.value)
