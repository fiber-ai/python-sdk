from enum import Enum


class SyncContactEnrichmentResponse200OutputProfileStatus(str, Enum):
    COMPLETED = "completed"
    FAILED = "failed"
    GRABBING_CONTACT_INFO = "grabbing-contact-info"
    LIVE_ENRICHING = "live-enriching"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
