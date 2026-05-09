from enum import Enum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType5LocationType(
    str, Enum
):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
