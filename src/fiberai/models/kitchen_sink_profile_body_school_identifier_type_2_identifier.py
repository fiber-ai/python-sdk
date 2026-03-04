from enum import Enum

class KitchenSinkProfileBodySchoolIdentifierType2Identifier(str, Enum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
