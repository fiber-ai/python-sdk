from enum import StrEnum


class JobPostingChangeLocationTypeType3Type1(StrEnum):
    HYBRID = "hybrid"
    ON_SITE = "on_site"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
