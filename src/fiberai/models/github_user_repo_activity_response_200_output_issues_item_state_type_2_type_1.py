from enum import StrEnum


class GithubUserRepoActivityResponse200OutputIssuesItemStateType2Type1(StrEnum):
    CLOSED = "closed"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
