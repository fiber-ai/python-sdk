from enum import Enum


class SyncCombinedSearchBodyCompanyParamsJobPostingStatsType0AllOfType0ItemType5LocationType(str, Enum):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
