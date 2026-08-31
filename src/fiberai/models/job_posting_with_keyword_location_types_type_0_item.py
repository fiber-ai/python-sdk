from enum import StrEnum


class JobPostingWithKeywordLocationTypesType0Item(StrEnum):
    HYBRID = "hybrid"
    ON_SITE = "on_site"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
