from enum import StrEnum


class GoogleMapsSearchBodyStrategyType2LargestCityTierIDType2Type1(StrEnum):
    LARGE = "large"
    MAJOR = "major"
    MEDIUM = "medium"
    MEGA = "mega"
    MINOR = "minor"
    SMALL = "small"
    TINY = "tiny"

    def __str__(self) -> str:
        return str(self.value)
