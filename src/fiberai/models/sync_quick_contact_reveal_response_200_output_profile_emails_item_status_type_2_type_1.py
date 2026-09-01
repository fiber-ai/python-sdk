from enum import StrEnum


class SyncQuickContactRevealResponse200OutputProfileEmailsItemStatusType2Type1(StrEnum):
    INVALID = "invalid"
    RISKY = "risky"
    UNKNOWN = "unknown"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
