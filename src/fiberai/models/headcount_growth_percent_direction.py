from enum import Enum


class HeadcountGrowthPercentDirection(str, Enum):
    EITHER = "either"
    GREW = "grew"
    SHRANK = "shrank"

    def __str__(self) -> str:
        return str(self.value)
