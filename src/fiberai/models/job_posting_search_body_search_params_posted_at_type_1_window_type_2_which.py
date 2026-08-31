from enum import StrEnum


class JobPostingSearchBodySearchParamsPostedAtType1WindowType2Which(StrEnum):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
