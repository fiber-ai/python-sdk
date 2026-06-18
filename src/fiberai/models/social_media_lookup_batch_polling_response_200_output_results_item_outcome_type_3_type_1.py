from enum import Enum


class SocialMediaLookupBatchPollingResponse200OutputResultsItemOutcomeType3Type1(str, Enum):
    FOUND_CANDIDATES = "FOUND_CANDIDATES"
    INSUFFICIENT_INFORMATION = "INSUFFICIENT_INFORMATION"
    NO_CANDIDATES_FOUND = "NO_CANDIDATES_FOUND"

    def __str__(self) -> str:
        return str(self.value)
