from enum import Enum

class GoogleMapsSearchBodyStrategyType1Strategy(str, Enum):
    SPECIFIC_AREAS = "specific-areas"

    def __str__(self) -> str:
        return str(self.value)
