from enum import Enum


class LiteContactRevealBodyInputType1Mode(str, Enum):
    NAME_DOMAIN = "name-domain"

    def __str__(self) -> str:
        return str(self.value)
