from enum import Enum


class GithubToLinkedinSingleResponse200OutputMatchSource(str, Enum):
    AGENT = "agent"
    EMAIL = "email"
    NAME_SEARCH = "name-search"
    NOT_FOUND = "not-found"
    WEB_SEARCH = "web-search"

    def __str__(self) -> str:
        return str(self.value)
