from enum import StrEnum


class FlightSearchResponse200OutputPriceInsightsType0PriceLevelType2Type1(StrEnum):
    HIGH = "high"
    LOW = "low"
    TYPICAL = "typical"

    def __str__(self) -> str:
        return str(self.value)
