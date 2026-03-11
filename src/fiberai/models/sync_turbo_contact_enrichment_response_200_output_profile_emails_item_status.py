from enum import Enum


class SyncTurboContactEnrichmentResponse200OutputProfileEmailsItemStatus(str, Enum):
    INVALID = "invalid"
    RISKY = "risky"
    UNKNOWN = "unknown"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
