from enum import StrEnum


class MultiSourceSearchBodySearchType1Request(StrEnum):
    SUBSEQUENT = "subsequent"

    def __str__(self) -> str:
        return str(self.value)
