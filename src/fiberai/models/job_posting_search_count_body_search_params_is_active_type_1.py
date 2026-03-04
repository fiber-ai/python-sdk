from enum import Enum

class JobPostingSearchCountBodySearchParamsIsActiveType1(str, Enum):
    FALSE = "false"
    NO_PREFERENCE = "no_preference"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
