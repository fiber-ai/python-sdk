from enum import StrEnum


class GithubToLinkedinSingleBodyOutputType(StrEnum):
    BOTH = "both"
    EMAIL = "email"
    LINKEDIN = "linkedin"

    def __str__(self) -> str:
        return str(self.value)
