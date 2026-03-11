from enum import Enum


class SyncCombinedSearchBodyProfileParamsJobStatusType2Status(str, Enum):
    EVER_EMPLOYED = "ever-employed"

    def __str__(self) -> str:
        return str(self.value)
