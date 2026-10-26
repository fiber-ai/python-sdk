from enum import StrEnum


class GithubUserRepoActivityResponse200OutputUnavailableSectionsItem(StrEnum):
    COMMITS = "commits"
    ISSUES = "issues"
    PULLREQUESTS = "pullRequests"

    def __str__(self) -> str:
        return str(self.value)
