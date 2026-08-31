from enum import StrEnum


class PollBatchLiveEnrichResponse200OutputType(StrEnum):
    COMPANY = "COMPANY"
    PROFILE = "PROFILE"

    def __str__(self) -> str:
        return str(self.value)
