from enum import StrEnum


class PollBatchLiveEnrichResponse200OutputStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"

    def __str__(self) -> str:
        return str(self.value)
