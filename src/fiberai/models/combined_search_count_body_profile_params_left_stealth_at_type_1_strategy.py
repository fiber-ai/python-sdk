from enum import Enum


class CombinedSearchCountBodyProfileParamsLeftStealthAtType1Strategy(str, Enum):
    RELATIVE = "relative"

    def __str__(self) -> str:
        return str(self.value)
