from enum import Enum


class PollBatchLiveEnrichResponse200OutputStatus(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"

    def __str__(self) -> str:
        return str(self.value)
