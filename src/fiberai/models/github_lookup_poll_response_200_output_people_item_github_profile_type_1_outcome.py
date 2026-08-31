from enum import StrEnum


class GithubLookupPollResponse200OutputPeopleItemGithubProfileType1Outcome(StrEnum):
    NOTFOUND = "notFound"

    def __str__(self) -> str:
        return str(self.value)
