from enum import Enum


class JdToProfileSearchBodySearchType1Request(str, Enum):
    SUBSEQUENT = "subsequent"

    def __str__(self) -> str:
        return str(self.value)
