from enum import StrEnum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsPastJobTextType0CriteriaItemField(StrEnum):
    ANYWHERE = "anywhere"
    SUMMARY = "summary"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
