from enum import StrEnum


class StartBatchLiveEnrichBodyType(StrEnum):
    COMPANY = "COMPANY"
    PROFILE = "PROFILE"

    def __str__(self) -> str:
        return str(self.value)
