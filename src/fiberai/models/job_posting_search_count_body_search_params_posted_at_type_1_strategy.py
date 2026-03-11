from enum import Enum


class JobPostingSearchCountBodySearchParamsPostedAtType1Strategy(str, Enum):
    RELATIVE = "relative"

    def __str__(self) -> str:
        return str(self.value)
