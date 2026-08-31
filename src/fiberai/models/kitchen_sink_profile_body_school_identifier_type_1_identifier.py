from enum import StrEnum


class KitchenSinkProfileBodySchoolIdentifierType1Identifier(StrEnum):
    LINKEDINURL = "linkedinUrl"

    def __str__(self) -> str:
        return str(self.value)
