from enum import Enum


class FlightSearchResponse200OutputPriceInsightsType0PriceLevelType2Type1(str, Enum):
    HIGH = "high"
    LOW = "low"
    TYPICAL = "typical"

    def __str__(self) -> str:
        return str(self.value)
