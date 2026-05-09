from enum import Enum


class GithubLookupPollResponse200OutputPeopleItemGithubProfileType1Outcome(str, Enum):
    NOTFOUND = "notFound"

    def __str__(self) -> str:
        return str(self.value)
