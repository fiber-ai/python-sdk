from enum import Enum


class MultiSourceSearchResponse200OutputDataType1Type(str, Enum):
    PROSPECTS = "prospects"

    def __str__(self) -> str:
        return str(self.value)
