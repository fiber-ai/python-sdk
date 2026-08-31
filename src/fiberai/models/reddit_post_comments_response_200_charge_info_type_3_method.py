from enum import StrEnum


class RedditPostCommentsResponse200ChargeInfoType3Method(StrEnum):
    FREE = "free"

    def __str__(self) -> str:
        return str(self.value)
