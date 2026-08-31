from enum import StrEnum


class SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType3Type1(StrEnum):
    FOUND_CANDIDATES = "FOUND_CANDIDATES"
    INSUFFICIENT_INFORMATION = "INSUFFICIENT_INFORMATION"
    NO_CANDIDATES_FOUND = "NO_CANDIDATES_FOUND"

    def __str__(self) -> str:
        return str(self.value)
