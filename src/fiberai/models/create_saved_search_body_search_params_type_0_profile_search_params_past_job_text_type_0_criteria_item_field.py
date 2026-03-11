from enum import Enum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsPastJobTextType0CriteriaItemField(str, Enum):
    ANYWHERE = "anywhere"
    SUMMARY = "summary"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
