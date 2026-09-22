from enum import StrEnum


class LiteContactRevealResponse200OutputProfileUnmatchedWorkEmailsItemValidationStatusType1(StrEnum):
    INVALID = "invalid"
    RISKY = "risky"
    UNKNOWN = "unknown"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
