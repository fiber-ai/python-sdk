from enum import Enum


class LiteContactRevealBodyInputType0Mode(str, Enum):
    LINKEDIN = "linkedin"

    def __str__(self) -> str:
        return str(self.value)
