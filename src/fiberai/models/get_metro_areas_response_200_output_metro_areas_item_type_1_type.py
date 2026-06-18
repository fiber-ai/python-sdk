from enum import Enum


class GetMetroAreasResponse200OutputMetroAreasItemType1Type(str, Enum):
    POLYGON = "polygon"

    def __str__(self) -> str:
        return str(self.value)
