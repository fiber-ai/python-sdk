from enum import Enum

class PollCombinedSearchBodyEntityType(str, Enum):
    COMPANY = "company"
    PROFILE = "profile"

    def __str__(self) -> str:
        return str(self.value)
