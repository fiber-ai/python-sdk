from enum import Enum


class CombinedSearchBodyProfileParamsPastJobTextType0CriteriaItemField(str, Enum):
    ANYWHERE = "anywhere"
    SUMMARY = "summary"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
