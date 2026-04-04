from enum import Enum


class TwitterTweetDetailsResponse200ChargeInfoType0Method(str, Enum):
    CHARGED_NOW = "charged-now"

    def __str__(self) -> str:
        return str(self.value)
