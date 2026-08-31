from enum import StrEnum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobsType0AllOfType0ItemStatus(StrEnum):
    ANY = "any"
    CURRENT = "current"
    PAST = "past"

    def __str__(self) -> str:
        return str(self.value)
