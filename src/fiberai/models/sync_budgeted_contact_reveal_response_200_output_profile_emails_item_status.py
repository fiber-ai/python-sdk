from enum import StrEnum


class SyncBudgetedContactRevealResponse200OutputProfileEmailsItemStatus(StrEnum):
    INVALID = "invalid"
    RISKY = "risky"
    UNKNOWN = "unknown"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
