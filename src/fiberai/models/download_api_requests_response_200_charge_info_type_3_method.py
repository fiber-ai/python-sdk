from enum import StrEnum


class DownloadApiRequestsResponse200ChargeInfoType3Method(StrEnum):
    FREE = "free"

    def __str__(self) -> str:
        return str(self.value)
