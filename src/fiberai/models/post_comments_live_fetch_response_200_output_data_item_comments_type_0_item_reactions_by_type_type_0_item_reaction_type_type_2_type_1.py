from enum import Enum


class PostCommentsLiveFetchResponse200OutputDataItemCommentsType0ItemReactionsByTypeType0ItemReactionTypeType2Type1(
    str, Enum
):
    CELEBRATE = "CELEBRATE"
    FUNNY = "FUNNY"
    INSIGHTFUL = "INSIGHTFUL"
    LIKE = "LIKE"
    LOVE = "LOVE"
    SUPPORT = "SUPPORT"

    def __str__(self) -> str:
        return str(self.value)
