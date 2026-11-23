from enum import StrEnum


class LookalikesBulkPollResponse200OutputStatus(StrEnum):
    DONE = "done"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
