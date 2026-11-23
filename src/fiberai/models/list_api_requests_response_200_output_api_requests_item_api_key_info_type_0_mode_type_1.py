from enum import StrEnum


class ListApiRequestsResponse200OutputApiRequestsItemApiKeyInfoType0ModeType1(StrEnum):
    LIVE = "LIVE"
    TEST = "TEST"

    def __str__(self) -> str:
        return str(self.value)
