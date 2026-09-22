from enum import StrEnum


class SyncTurboContactEnrichmentResponse200OutputProfileUnmatchedWorkEmailsItemStatusType1(StrEnum):
    INVALID = "invalid"
    RISKY = "risky"
    UNKNOWN = "unknown"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
