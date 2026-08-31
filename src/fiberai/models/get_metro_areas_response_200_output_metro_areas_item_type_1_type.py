from enum import StrEnum


class GetMetroAreasResponse200OutputMetroAreasItemType1Type(StrEnum):
    POLYGON = "polygon"

    def __str__(self) -> str:
        return str(self.value)
