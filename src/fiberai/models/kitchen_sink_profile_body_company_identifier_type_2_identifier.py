from enum import Enum


class KitchenSinkProfileBodyCompanyIdentifierType2Identifier(str, Enum):
    LINKEDINORGID = "linkedinOrgID"

    def __str__(self) -> str:
        return str(self.value)
