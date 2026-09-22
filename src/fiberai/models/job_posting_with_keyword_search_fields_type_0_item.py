from enum import StrEnum


class JobPostingWithKeywordSearchFieldsType0Item(StrEnum):
    DESCRIPTION = "description"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
