from enum import Enum

class PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0EmailsItemStatus(str, Enum):
    INVALID = "invalid"
    RISKY = "risky"
    UNKNOWN = "unknown"
    VALID = "valid"

    def __str__(self) -> str:
        return str(self.value)
