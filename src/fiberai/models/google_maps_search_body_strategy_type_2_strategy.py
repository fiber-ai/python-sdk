from enum import StrEnum


class GoogleMapsSearchBodyStrategyType2Strategy(StrEnum):
    WORLD_CITIES = "world-cities"

    def __str__(self) -> str:
        return str(self.value)
