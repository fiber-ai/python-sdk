from enum import StrEnum


class PeopleSearchCountBodySearchParamsPastJobTextType0CriteriaItemRule(StrEnum):
    EXCLUDES = "excludes"
    INCLUDES = "includes"

    def __str__(self) -> str:
        return str(self.value)
