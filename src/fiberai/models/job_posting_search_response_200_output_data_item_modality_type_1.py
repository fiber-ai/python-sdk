from enum import StrEnum


class JobPostingSearchResponse200OutputDataItemModalityType1(StrEnum):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
