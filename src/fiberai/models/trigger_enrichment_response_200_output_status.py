from enum import Enum


class TriggerEnrichmentResponse200OutputStatus(str, Enum):
    NOT_STARTED = "NOT_STARTED"

    def __str__(self) -> str:
        return str(self.value)
