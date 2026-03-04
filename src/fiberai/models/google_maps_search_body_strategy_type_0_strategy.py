from enum import Enum

class GoogleMapsSearchBodyStrategyType0Strategy(str, Enum):
    WHOLE_USA = "whole-usa"

    def __str__(self) -> str:
        return str(self.value)
