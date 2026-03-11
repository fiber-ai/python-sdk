from enum import Enum


class KitchenSinkBulkProfileBodyProfilesItemCompanyIdentifierType2Identifier(str, Enum):
    LINKEDINORGID = "linkedinOrgID"

    def __str__(self) -> str:
        return str(self.value)
