from enum import Enum


class CombinedSearchBodyProfileParamsJobStatusType1Status(str, Enum):
    PREVIOUSLY_EMPLOYED = "previously-employed"

    def __str__(self) -> str:
        return str(self.value)
