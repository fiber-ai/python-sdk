from enum import Enum


class GithubLookupPollingResponse200OutputDataItemOutcomeType1(str, Enum):
    FOUND_CANDIDATES = "FOUND_CANDIDATES"
    INSUFFICIENT_INFORMATION = "INSUFFICIENT_INFORMATION"
    NO_CANDIDATES_FOUND = "NO_CANDIDATES_FOUND"

    def __str__(self) -> str:
        return str(self.value)
