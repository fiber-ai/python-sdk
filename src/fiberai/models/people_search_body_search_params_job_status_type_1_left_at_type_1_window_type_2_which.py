from enum import StrEnum


class PeopleSearchBodySearchParamsJobStatusType1LeftAtType1WindowType2Which(StrEnum):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
