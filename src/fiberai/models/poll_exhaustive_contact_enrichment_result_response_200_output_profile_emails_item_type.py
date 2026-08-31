from enum import StrEnum


class PollExhaustiveContactEnrichmentResultResponse200OutputProfileEmailsItemType(StrEnum):
    GENERIC = "generic"
    OTHER = "other"
    PERSONAL = "personal"
    UNKNOWN = "unknown"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
