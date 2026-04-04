from enum import Enum


class MultiSourceSearchBodySearchType1Request(str, Enum):
    SUBSEQUENT = "subsequent"

    def __str__(self) -> str:
        return str(self.value)
