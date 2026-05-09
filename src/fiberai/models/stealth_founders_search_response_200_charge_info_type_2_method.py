from enum import Enum


class StealthFoundersSearchResponse200ChargeInfoType2Method(str, Enum):
    CHARGED_FOR_ASYNC_PROCESS = "charged-for-async-process"

    def __str__(self) -> str:
        return str(self.value)
