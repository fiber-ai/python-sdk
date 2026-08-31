from enum import StrEnum


class LiteContactRevealBodyInputType1Mode(StrEnum):
    NAME_DOMAIN = "name-domain"

    def __str__(self) -> str:
        return str(self.value)
