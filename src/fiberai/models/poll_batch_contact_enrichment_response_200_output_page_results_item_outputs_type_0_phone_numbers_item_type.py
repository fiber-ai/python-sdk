from enum import Enum

class PollBatchContactEnrichmentResponse200OutputPageResultsItemOutputsType0PhoneNumbersItemType(str, Enum):
    MOBILE = "mobile"
    OTHER = "other"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
