from enum import Enum


class YoutubeVideoCommentsResponse200ChargeInfoType3Method(str, Enum):
    FREE = "free"

    def __str__(self) -> str:
        return str(self.value)
