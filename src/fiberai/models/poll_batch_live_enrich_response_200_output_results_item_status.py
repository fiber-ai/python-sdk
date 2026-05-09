from enum import Enum


class PollBatchLiveEnrichResponse200OutputResultsItemStatus(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    MALFORMED = "MALFORMED"
    NOT_FOUND = "NOT_FOUND"

    def __str__(self) -> str:
        return str(self.value)
