from enum import Enum

class EmailBounceDetectionResponse200OutputVerdict(str, Enum):
    INCONCLUSIVE = "inconclusive"
    OK = "ok"
    RISKY = "risky"
    UNDELIVERABLE = "undeliverable"

    def __str__(self) -> str:
        return str(self.value)
