from enum import StrEnum


class FacebookPostCommentsBodySortType1(StrEnum):
    ALL = "all"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
