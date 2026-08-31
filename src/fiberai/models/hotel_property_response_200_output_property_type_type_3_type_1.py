from enum import StrEnum


class HotelPropertyResponse200OutputPropertyTypeType3Type1(StrEnum):
    HOTEL = "hotel"
    VACATIONRENTAL = "vacationRental"

    def __str__(self) -> str:
        return str(self.value)
