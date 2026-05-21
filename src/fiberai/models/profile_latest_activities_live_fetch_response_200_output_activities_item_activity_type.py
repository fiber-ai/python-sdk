from enum import Enum


class ProfileLatestActivitiesLiveFetchResponse200OutputActivitiesItemActivityType(str, Enum):
    COMMENT = "comment"
    OTHER = "other"
    POST = "post"
    REACTION = "reaction"
    REPOST = "repost"
    SHARE = "share"

    def __str__(self) -> str:
        return str(self.value)
