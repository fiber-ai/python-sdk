from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsPastJobTextType0CriteriaItemRule(StrEnum):
    EXCLUDES = "excludes"
    INCLUDES = "includes"

    def __str__(self) -> str:
        return str(self.value)
