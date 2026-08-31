from enum import StrEnum


class HotelPropertyResponse200OutputPropertyTypeType1(StrEnum):
    HOTEL = "hotel"
    VACATIONRENTAL = "vacationRental"

    def __str__(self) -> str:
        return str(self.value)
