from enum import StrEnum


class EmailBounceDetectionResponse200OutputVerdict(StrEnum):
    INCONCLUSIVE = "inconclusive"
    OK = "ok"
    RISKY = "risky"
    UNDELIVERABLE = "undeliverable"

    def __str__(self) -> str:
        return str(self.value)
