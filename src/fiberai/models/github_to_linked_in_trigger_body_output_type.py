from enum import StrEnum


class GithubToLinkedInTriggerBodyOutputType(StrEnum):
    BOTH = "both"
    EMAIL = "email"
    LINKEDIN = "linkedin"

    def __str__(self) -> str:
        return str(self.value)
