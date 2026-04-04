from enum import Enum


class MultiSourceSearchBodySearchType0Request(str, Enum):
    INITIAL = "initial"

    def __str__(self) -> str:
        return str(self.value)
