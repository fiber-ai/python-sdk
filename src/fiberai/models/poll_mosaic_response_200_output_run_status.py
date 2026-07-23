from enum import Enum


class PollMosaicResponse200OutputRunStatus(str, Enum):
    DONE = "done"
    FAILED = "failed"
    PENDING = "pending"
    RUNNING = "running"

    def __str__(self) -> str:
        return str(self.value)
