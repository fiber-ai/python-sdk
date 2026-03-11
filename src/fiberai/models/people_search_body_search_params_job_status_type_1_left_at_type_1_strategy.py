from enum import Enum


class PeopleSearchBodySearchParamsJobStatusType1LeftAtType1Strategy(str, Enum):
    RELATIVE = "relative"

    def __str__(self) -> str:
        return str(self.value)
