from enum import StrEnum


class FlightSearchResponse200OutputPriceInsightsType0PriceLevelType3Type1(StrEnum):
    HIGH = "high"
    LOW = "low"
    TYPICAL = "typical"

    def __str__(self) -> str:
        return str(self.value)
