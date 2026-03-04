from enum import Enum

class DomainLookupPollingResponse200OutputStatus(str, Enum):
    DONE = "DONE"
    FAILED = "FAILED"
    NOT_STARTED = "NOT_STARTED"
    STARTED = "STARTED"

    def __str__(self) -> str:
        return str(self.value)
