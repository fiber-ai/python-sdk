from enum import Enum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPastJobTextType0CriteriaItemRule(str, Enum):
    EXCLUDES = "excludes"
    INCLUDES = "includes"

    def __str__(self) -> str:
        return str(self.value)
