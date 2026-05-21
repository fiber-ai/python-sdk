from enum import Enum


class TiktokSongVideosResponse200ChargeInfoType4Method(str, Enum):
    CREDITS_REFUNDED = "credits-refunded"

    def __str__(self) -> str:
        return str(self.value)
