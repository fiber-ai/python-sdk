from enum import StrEnum


class PremiumPhoneRevealBodyPatienceType2Type1(StrEnum):
    EXTREME = "EXTREME"
    HIGH = "HIGH"
    LOW = "LOW"
    MAXIMUM = "MAXIMUM"
    MEDIUM = "MEDIUM"
    MINIMUM = "MINIMUM"

    def __str__(self) -> str:
        return str(self.value)
