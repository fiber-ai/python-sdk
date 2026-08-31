from enum import StrEnum


class RedditSubredditPostsBodySort(StrEnum):
    BEST = "best"
    HOT = "hot"
    NEW = "new"
    RISING = "rising"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
