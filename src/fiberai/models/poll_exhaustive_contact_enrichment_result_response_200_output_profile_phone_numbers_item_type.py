from enum import StrEnum


class PollExhaustiveContactEnrichmentResultResponse200OutputProfilePhoneNumbersItemType(StrEnum):
    MOBILE = "mobile"
    OTHER = "other"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
