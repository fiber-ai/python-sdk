from enum import StrEnum


class GithubOrgContributorsPollResponse200OutputSkippedReposItemReason(StrEnum):
    NOT_FOUND = "not_found"
    SCAN_FAILED = "scan_failed"
    TOO_LARGE = "too_large"

    def __str__(self) -> str:
        return str(self.value)
