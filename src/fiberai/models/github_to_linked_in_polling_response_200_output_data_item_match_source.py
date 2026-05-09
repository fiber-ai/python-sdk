from enum import Enum


class GithubToLinkedInPollingResponse200OutputDataItemMatchSource(str, Enum):
    AGENT = "agent"
    EMAIL = "email"
    NAME_SEARCH = "name-search"
    NOT_FOUND = "not-found"
    WEB_SEARCH = "web-search"

    def __str__(self) -> str:
        return str(self.value)
