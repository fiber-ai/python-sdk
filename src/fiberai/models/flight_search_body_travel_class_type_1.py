from enum import Enum


class FlightSearchBodyTravelClassType1(str, Enum):
    BUSINESS = "business"
    ECONOMY = "economy"
    FIRST = "first"
    PREMIUMECONOMY = "premiumEconomy"

    def __str__(self) -> str:
        return str(self.value)
