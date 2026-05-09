from enum import Enum


class GithubLookupPollResponse200OutputPeopleItemGithubProfileType2Outcome(str, Enum):
    INVALIDINPUT = "invalidInput"

    def __str__(self) -> str:
        return str(self.value)
