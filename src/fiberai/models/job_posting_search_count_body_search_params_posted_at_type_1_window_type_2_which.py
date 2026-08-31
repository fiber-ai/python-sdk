from enum import StrEnum


class JobPostingSearchCountBodySearchParamsPostedAtType1WindowType2Which(StrEnum):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
