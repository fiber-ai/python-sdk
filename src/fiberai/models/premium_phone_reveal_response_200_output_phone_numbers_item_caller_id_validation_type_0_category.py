from enum import Enum


class PremiumPhoneRevealResponse200OutputPhoneNumbersItemCallerIdValidationType0Category(str, Enum):
    BUSINESS_LINE = "BUSINESS_LINE"
    EXACT_MATCH = "EXACT_MATCH"
    FAMILY_MEMBER = "FAMILY_MEMBER"
    INCONCLUSIVE = "INCONCLUSIVE"
    PROBABLE_MATCH = "PROBABLE_MATCH"

    def __str__(self) -> str:
        return str(self.value)
