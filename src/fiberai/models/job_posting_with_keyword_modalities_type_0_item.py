from enum import StrEnum


class JobPostingWithKeywordModalitiesType0Item(StrEnum):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
