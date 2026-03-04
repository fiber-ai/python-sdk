from enum import Enum

class SyncCombinedSearchBodyProfileParamsPastJobTextType0Joiner(str, Enum):
    AND = "and"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
