from enum import Enum


class JobPostingChangeLocationTypeType2Type1(str, Enum):
    HYBRID = "hybrid"
    ON_SITE = "on_site"
    REMOTE = "remote"

    def __str__(self) -> str:
        return str(self.value)
