from enum import Enum


class GetMetroAreasResponse200OutputMetroAreasItemType0Type(str, Enum):
    CIRCLE = "circle"

    def __str__(self) -> str:
        return str(self.value)
