from enum import StrEnum


class HeadcountGrowthPercentDirection(StrEnum):
    EITHER = "either"
    GREW = "grew"
    SHRANK = "shrank"

    def __str__(self) -> str:
        return str(self.value)
