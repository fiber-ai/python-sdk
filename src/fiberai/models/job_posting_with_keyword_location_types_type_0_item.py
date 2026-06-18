from enum import Enum


class JobPostingWithKeywordLocationTypesType0Item(str, Enum):
    HYBRID = "hybrid"
    ON_SITE = "on_site"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
