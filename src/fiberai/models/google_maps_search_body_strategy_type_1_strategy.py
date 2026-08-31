from enum import StrEnum


class GoogleMapsSearchBodyStrategyType1Strategy(StrEnum):
    SPECIFIC_AREAS = "specific-areas"

    def __str__(self) -> str:
        return str(self.value)
