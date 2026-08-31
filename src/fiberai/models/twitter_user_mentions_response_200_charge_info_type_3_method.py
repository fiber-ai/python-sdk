from enum import StrEnum


class TwitterUserMentionsResponse200ChargeInfoType3Method(StrEnum):
    FREE = "free"

    def __str__(self) -> str:
        return str(self.value)
