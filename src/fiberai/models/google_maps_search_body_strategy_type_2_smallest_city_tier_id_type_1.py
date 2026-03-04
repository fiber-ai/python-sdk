from enum import Enum

class GoogleMapsSearchBodyStrategyType2SmallestCityTierIDType1(str, Enum):
    LARGE = "large"
    MAJOR = "major"
    MEDIUM = "medium"
    MEGA = "mega"
    MINOR = "minor"
    SMALL = "small"
    TINY = "tiny"

    def __str__(self) -> str:
        return str(self.value)
