from enum import StrEnum


class JobPostingSearchBodySearchParamsIsActiveType1(StrEnum):
    FALSE = "false"
    NO_PREFERENCE = "no_preference"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
