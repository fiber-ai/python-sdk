from enum import StrEnum


class PeopleSearchBodySearchParamsStartedInRoleType1WindowType2Which(StrEnum):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
