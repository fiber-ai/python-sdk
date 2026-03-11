from enum import Enum


class GithubToLinkedInPollingResponse200OutputDataItemMatchSource(str, Enum):
    EMAIL_APOLLO = "email-apollo"
    EMAIL_AVIATO = "email-aviato"
    EMAIL_ELASTIC = "email-elastic"
    KITCHEN_SINK_AGENT = "kitchen-sink-agent"
    NAME_SEARCH = "name-search"
    NAME_SEARCH_LLM = "name-search-llm"
    NOT_FOUND = "not-found"
    WEB_SEARCH = "web-search"
    WEB_SEARCH_AGENT = "web-search-agent"

    def __str__(self) -> str:
        return str(self.value)
