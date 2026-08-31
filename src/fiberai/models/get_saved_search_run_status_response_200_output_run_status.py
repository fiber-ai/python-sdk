from enum import StrEnum


class GetSavedSearchRunStatusResponse200OutputRunStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    NOT_STARTED = "NOT_STARTED"
    PROCESSING = "PROCESSING"
    REJECTED_NO_FUNDS = "REJECTED_NO_FUNDS"

    def __str__(self) -> str:
        return str(self.value)
