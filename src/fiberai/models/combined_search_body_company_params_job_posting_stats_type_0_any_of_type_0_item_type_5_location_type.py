from enum import Enum


class CombinedSearchBodyCompanyParamsJobPostingStatsType0AnyOfType0ItemType5LocationType(str, Enum):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
