from enum import StrEnum


class PollBatchContactDetailsResponse200OutputPageResultsItemOutputsType0EmailsItemType(StrEnum):
    GENERIC = "generic"
    OTHER = "other"
    PERSONAL = "personal"
    UNKNOWN = "unknown"
    WORK = "work"

    def __str__(self) -> str:
        return str(self.value)
