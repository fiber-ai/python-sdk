from enum import StrEnum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobsType0AllOfType0ItemStatus(StrEnum):
    ANY = "any"
    CURRENT = "current"
    PAST = "past"

    def __str__(self) -> str:
        return str(self.value)
