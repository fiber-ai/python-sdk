from enum import Enum


class GithubToLinkedinSingleResponse200OutputDebugTimingsType0ResolverStepsItemOutcome(str, Enum):
    ERROR = "error"
    HIT = "hit"
    MISS = "miss"
    SKIPPED = "skipped"

    def __str__(self) -> str:
        return str(self.value)
