from enum import Enum

class CheckGoogleMapsResultsResponse200OutputStatus(str, Enum):
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    NOT_STARTED = "NOT_STARTED"
    RUNNING = "RUNNING"

    def __str__(self) -> str:
        return str(self.value)
