from enum import Enum

class SyncCombinedSearchBodyProfileParamsPastJobTextType0CriteriaItemRule(str, Enum):
    EXCLUDES = "excludes"
    INCLUDES = "includes"

    def __str__(self) -> str:
        return str(self.value)
