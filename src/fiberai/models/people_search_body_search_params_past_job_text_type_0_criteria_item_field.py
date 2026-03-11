from enum import Enum


class PeopleSearchBodySearchParamsPastJobTextType0CriteriaItemField(str, Enum):
    ANYWHERE = "anywhere"
    SUMMARY = "summary"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
