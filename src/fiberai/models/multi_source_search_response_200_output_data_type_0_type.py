from enum import Enum


class MultiSourceSearchResponse200OutputDataType0Type(str, Enum):
    COMPANIES = "companies"

    def __str__(self) -> str:
        return str(self.value)
