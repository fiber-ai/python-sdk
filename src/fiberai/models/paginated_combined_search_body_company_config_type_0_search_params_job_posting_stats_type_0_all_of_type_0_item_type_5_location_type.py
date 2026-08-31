from enum import StrEnum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0AllOfType0ItemType5LocationType(
    StrEnum
):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
