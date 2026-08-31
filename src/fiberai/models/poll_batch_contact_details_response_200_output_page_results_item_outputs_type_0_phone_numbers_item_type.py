from enum import StrEnum


class PollBatchContactDetailsResponse200OutputPageResultsItemOutputsType0PhoneNumbersItemType(StrEnum):
    MOBILE = "mobile"
    OTHER = "other"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return str(self.value)
