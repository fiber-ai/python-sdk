from enum import StrEnum


class MultiSourceSearchResponse200OutputDataType1Type(StrEnum):
    PROSPECTS = "prospects"

    def __str__(self) -> str:
        return str(self.value)
