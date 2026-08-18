from enum import Enum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsJobsType0AllOfType0ItemStatus(str, Enum):
    ANY = "any"
    CURRENT = "current"
    PAST = "past"

    def __str__(self) -> str:
        return str(self.value)
