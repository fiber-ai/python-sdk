from enum import Enum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPastJobTextType0CriteriaItemField(str, Enum):
    ANYWHERE = "anywhere"
    SUMMARY = "summary"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
