from enum import Enum


class LiteContactRevealBodyPatienceType2Type1(str, Enum):
    EXTREME = "EXTREME"
    HIGH = "HIGH"
    LOW = "LOW"
    MAXIMUM = "MAXIMUM"
    MEDIUM = "MEDIUM"
    MINIMUM = "MINIMUM"

    def __str__(self) -> str:
        return str(self.value)
