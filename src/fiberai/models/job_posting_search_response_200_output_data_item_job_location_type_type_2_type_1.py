from enum import Enum


class JobPostingSearchResponse200OutputDataItemJobLocationTypeType2Type1(str, Enum):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
