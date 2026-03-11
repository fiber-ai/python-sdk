from enum import Enum


class PollContactEnrichmentResultResponse200OutputProfileEmailsItemType(str, Enum):
    GENERIC = "generic"
    OTHER = "other"
    PERSONAL = "personal"
    UNKNOWN = "unknown"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
