from enum import Enum


class LocationTypeaheadResponse200OutputPresetRegionsItemType1Type(str, Enum):
    POLYGON = "polygon"

    def __str__(self) -> str:
        return str(self.value)
