from enum import Enum

class CombinedSearchBodyProfileParamsCompanyMatchModeType1Mode(str, Enum):
    LOOSE = "loose"

    def __str__(self) -> str:
        return str(self.value)
