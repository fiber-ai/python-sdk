from enum import Enum


class GoogleMapsSearchBodyStrategyType1UnionAllItemType1RegionType(str, Enum):
    RECTANGLE = "rectangle"

    def __str__(self) -> str:
        return str(self.value)
