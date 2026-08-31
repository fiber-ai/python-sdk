from enum import StrEnum


class KitchenSinkProfileBodyProfileIdentifierType1Identifier(StrEnum):
    LINKEDINURL = "linkedinUrl"

    def __str__(self) -> str:
        return str(self.value)
