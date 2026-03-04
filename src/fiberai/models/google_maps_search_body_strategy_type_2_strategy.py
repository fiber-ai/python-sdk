from enum import Enum

class GoogleMapsSearchBodyStrategyType2Strategy(str, Enum):
    WORLD_CITIES = "world-cities"

    def __str__(self) -> str:
        return str(self.value)
