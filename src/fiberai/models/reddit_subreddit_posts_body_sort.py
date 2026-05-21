from enum import Enum


class RedditSubredditPostsBodySort(str, Enum):
    BEST = "best"
    HOT = "hot"
    NEW = "new"
    RISING = "rising"
    TOP = "top"

    def __str__(self) -> str:
        return str(self.value)
