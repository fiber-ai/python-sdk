from enum import StrEnum


class SyncTurboContactEnrichmentResponse200OutputProfileStatus(StrEnum):
    COMPLETED = "completed"

    def __str__(self) -> str:
        return str(self.value)
