from enum import StrEnum


class PeopleSearchCountBodySearchParamsPastJobTextType0CriteriaItemField(StrEnum):
    ANYWHERE = "anywhere"
    SUMMARY = "summary"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
