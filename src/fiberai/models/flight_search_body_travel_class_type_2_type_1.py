from enum import StrEnum


class FlightSearchBodyTravelClassType2Type1(StrEnum):
    BUSINESS = "business"
    ECONOMY = "economy"
    FIRST = "first"
    PREMIUMECONOMY = "premiumEconomy"

    def __str__(self) -> str:
        return str(self.value)
