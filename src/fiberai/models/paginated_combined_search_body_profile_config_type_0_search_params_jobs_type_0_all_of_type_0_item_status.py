from enum import Enum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemStatus(str, Enum):
    ANY = "any"
    CURRENT = "current"
    PAST = "past"

    def __str__(self) -> str:
        return str(self.value)
