from enum import Enum


class SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatusType1(str, Enum):
    INVALID = "invalid"
    RISKY = "risky"
    UNKNOWN = "unknown"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
