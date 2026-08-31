from enum import StrEnum


class TriggerEnrichmentResponse200OutputStatus(StrEnum):
    NOT_STARTED = "NOT_STARTED"

    def __str__(self) -> str:
        return str(self.value)
