from enum import StrEnum


class RedditSubredditSearchBodySort(StrEnum):
    COMMENT_COUNT = "comment_count"
    HOT = "hot"
    NEW = "new"
    RELEVANCE = "relevance"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
