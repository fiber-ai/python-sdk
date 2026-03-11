from enum import Enum


class JobPostingSearchResponse200OutputDataItemJobLocationTypeType1(str, Enum):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
