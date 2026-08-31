from enum import StrEnum


class RedditSearchBodySort(StrEnum):
    COMMENT_COUNT = "comment_count"
    NEW = "new"
    RELEVANCE = "relevance"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
