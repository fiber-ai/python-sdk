from enum import StrEnum


class HotelSearchResponse200OutputPropertiesItemTypeType1(StrEnum):
    HOTEL = "hotel"
    VACATIONRENTAL = "vacationRental"

    def __str__(self) -> str:
        return str(self.value)
