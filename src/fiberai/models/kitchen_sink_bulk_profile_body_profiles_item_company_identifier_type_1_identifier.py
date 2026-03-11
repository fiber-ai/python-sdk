from enum import Enum


class KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType1Identifier(str, Enum):
    LINKEDINURL = "linkedinUrl"

    def __str__(self) -> str:
        return str(self.value)
