from enum import StrEnum


class PollBatchLiveEnrichResponse200OutputResultsItemStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    MALFORMED = "MALFORMED"
    NOT_FOUND = "NOT_FOUND"

    def __str__(self) -> str:
        return str(self.value)
