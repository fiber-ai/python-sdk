from enum import Enum

class PeopleSearchCountBodySearchParamsPastJobTextType0CriteriaItemRule(str, Enum):
    EXCLUDES = "excludes"
    INCLUDES = "includes"

    def __str__(self) -> str:
        return str(self.value)
