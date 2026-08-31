from enum import StrEnum


class PeopleSearchBodySearchParamsPastJobTextType0CriteriaItemRule(StrEnum):
    EXCLUDES = "excludes"
    INCLUDES = "includes"

    def __str__(self) -> str:
        return str(self.value)
