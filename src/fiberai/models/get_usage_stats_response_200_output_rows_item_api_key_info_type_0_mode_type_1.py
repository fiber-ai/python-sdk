from enum import StrEnum


class GetUsageStatsResponse200OutputRowsItemApiKeyInfoType0ModeType1(StrEnum):
    LIVE = "LIVE"
    TEST = "TEST"

    def __str__(self) -> str:
        return str(self.value)
