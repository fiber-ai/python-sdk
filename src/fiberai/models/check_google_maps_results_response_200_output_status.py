from enum import StrEnum


class CheckGoogleMapsResultsResponse200OutputStatus(StrEnum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    NOT_STARTED = "NOT_STARTED"
    RUNNING = "RUNNING"

    def __str__(self) -> str:
        return str(self.value)
