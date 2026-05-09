from enum import Enum


class PollBatchLiveEnrichResponse200OutputType(str, Enum):
    COMPANY = "COMPANY"
    PROFILE = "PROFILE"

    def __str__(self) -> str:
        return str(self.value)
