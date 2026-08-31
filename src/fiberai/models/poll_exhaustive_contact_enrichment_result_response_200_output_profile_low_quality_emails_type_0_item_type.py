from enum import StrEnum


class PollExhaustiveContactEnrichmentResultResponse200OutputProfileLowQualityEmailsType0ItemType(StrEnum):
    GENERIC = "generic"
    OTHER = "other"
    PERSONAL = "personal"
    UNKNOWN = "unknown"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
