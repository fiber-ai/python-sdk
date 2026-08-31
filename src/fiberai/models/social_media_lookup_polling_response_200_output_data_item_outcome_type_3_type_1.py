from enum import StrEnum


class SocialMediaLookupPollingResponse200OutputDataItemOutcomeType3Type1(StrEnum):
    FOUND_CANDIDATES = "FOUND_CANDIDATES"
    INSUFFICIENT_INFORMATION = "INSUFFICIENT_INFORMATION"
    NO_CANDIDATES_FOUND = "NO_CANDIDATES_FOUND"

    def __str__(self) -> str:
        return str(self.value)
