from enum import Enum


class CombinedSearchCountBodyProfileParamsPastJobTextType0CriteriaItemRule(str, Enum):
    EXCLUDES = "excludes"
    INCLUDES = "includes"

    def __str__(self) -> str:
        return str(self.value)
