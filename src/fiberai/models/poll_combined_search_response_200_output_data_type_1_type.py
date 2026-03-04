from enum import Enum

class PollCombinedSearchResponse200OutputDataType1Type(str, Enum):
    PROFILES = "profiles"

    def __str__(self) -> str:
        return str(self.value)
