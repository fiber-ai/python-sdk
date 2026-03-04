from enum import Enum

class KitchenSinkProfileBodySchoolIdentifierType1Identifier(str, Enum):
    LINKEDINURL = "linkedinUrl"

    def __str__(self) -> str:
        return str(self.value)
