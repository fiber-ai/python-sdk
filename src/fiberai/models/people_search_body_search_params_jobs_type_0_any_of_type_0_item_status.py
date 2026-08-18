from enum import Enum


class PeopleSearchBodySearchParamsJobsType0AnyOfType0ItemStatus(str, Enum):
    ANY = "any"
    CURRENT = "current"
    PAST = "past"

    def __str__(self) -> str:
        return str(self.value)
