from enum import Enum


class JdToProfileSearchResponse200OutputSearchParamsStealthV2Type0Status(str, Enum):
    CURRENTLY_IN_STEALTH = "currently-in-stealth"

    def __str__(self) -> str:
        return str(self.value)
