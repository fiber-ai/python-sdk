from enum import StrEnum


class PostCommentsLiveFetchResponse200OutputDataItemReactionsByTypeType0ItemReactionTypeType1(StrEnum):
    CELEBRATE = "CELEBRATE"
    FUNNY = "FUNNY"
    INSIGHTFUL = "INSIGHTFUL"
    LIKE = "LIKE"
    LOVE = "LOVE"
    SUPPORT = "SUPPORT"

    def __str__(self) -> str:
        return str(self.value)
