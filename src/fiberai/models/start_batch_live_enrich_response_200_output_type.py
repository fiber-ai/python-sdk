from enum import Enum


class StartBatchLiveEnrichResponse200OutputType(str, Enum):
    COMPANY = "COMPANY"
    PROFILE = "PROFILE"

    def __str__(self) -> str:
        return str(self.value)
