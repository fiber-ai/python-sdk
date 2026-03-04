from enum import Enum

class PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemType(str, Enum):
    GENERIC = "generic"
    OTHER = "other"
    PERSONAL = "personal"
    UNKNOWN = "unknown"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
