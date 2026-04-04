from enum import Enum


class CombinedSearchCountBodyCompanyParamsFoundedOnType1Strategy(str, Enum):
    RELATIVE = "relative"

    def __str__(self) -> str:
        return str(self.value)
