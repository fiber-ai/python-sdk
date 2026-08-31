from enum import StrEnum


class PollExhaustiveContactEnrichmentResultResponse200OutputProfileStatus(StrEnum):
    COMPLETED = "completed"
    FAILED = "failed"
    GRABBING_CONTACT_INFO = "grabbing-contact-info"
    LIVE_ENRICHING = "live-enriching"
    STARTED = "started"

    def __str__(self) -> str:
        return str(self.value)
