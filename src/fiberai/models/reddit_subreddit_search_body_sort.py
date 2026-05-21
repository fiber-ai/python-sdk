from enum import Enum


class RedditSubredditSearchBodySort(str, Enum):
    COMMENT_COUNT = "comment_count"
    HOT = "hot"
    NEW = "new"
    RELEVANCE = "relevance"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
