from enum import Enum


class GithubToLinkedinSingleBodyOutputType(str, Enum):
    BOTH = "both"
    EMAIL = "email"
    LINKEDIN = "linkedin"

    def __str__(self) -> str:
        return str(self.value)
