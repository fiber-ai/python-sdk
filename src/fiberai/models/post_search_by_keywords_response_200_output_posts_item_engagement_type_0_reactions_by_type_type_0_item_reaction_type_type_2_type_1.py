from enum import StrEnum


class PostSearchByKeywordsResponse200OutputPostsItemEngagementType0ReactionsByTypeType0ItemReactionTypeType2Type1(
    StrEnum
):
    CELEBRATE = "CELEBRATE"
    FUNNY = "FUNNY"
    INSIGHTFUL = "INSIGHTFUL"
    LIKE = "LIKE"
    LOVE = "LOVE"
    SUPPORT = "SUPPORT"

    def __str__(self) -> str:
        return str(self.value)
