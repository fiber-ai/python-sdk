from enum import StrEnum


class FacebookGroupPostsBodySortType2Type1(StrEnum):
    CHRONOLOGICAL = "chronological"
    RECENT_ACTIVITY = "recent_activity"
    TOP_POSTS = "top_posts"

    def __str__(self) -> str:
        return str(self.value)
