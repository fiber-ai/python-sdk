from enum import StrEnum


class PostReactionsLiveFetchBodyReactionTypeType1(StrEnum):
    CELEBRATE = "CELEBRATE"
    CURIOUS = "CURIOUS"
    FUNNY = "FUNNY"
    INSIGHTFUL = "INSIGHTFUL"
    LIKE = "LIKE"
    LOVE = "LOVE"
    SUPPORT = "SUPPORT"

    def __str__(self) -> str:
        return str(self.value)
