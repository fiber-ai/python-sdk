from enum import StrEnum


class GithubToLinkedInPollingResponse200OutputDataItemStatus(StrEnum):
    DONE = "DONE"
    FAILED = "FAILED"
    NOT_STARTED = "NOT_STARTED"
    STARTED = "STARTED"

    def __str__(self) -> str:
        return str(self.value)
