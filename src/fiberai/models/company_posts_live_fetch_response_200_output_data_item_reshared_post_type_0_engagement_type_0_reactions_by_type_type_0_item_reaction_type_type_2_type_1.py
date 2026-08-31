from enum import StrEnum


class CompanyPostsLiveFetchResponse200OutputDataItemResharedPostType0EngagementType0ReactionsByTypeType0ItemReactionTypeType2Type1(
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
