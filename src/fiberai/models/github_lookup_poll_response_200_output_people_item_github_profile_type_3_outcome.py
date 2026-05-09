from enum import Enum


class GithubLookupPollResponse200OutputPeopleItemGithubProfileType3Outcome(str, Enum):
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
