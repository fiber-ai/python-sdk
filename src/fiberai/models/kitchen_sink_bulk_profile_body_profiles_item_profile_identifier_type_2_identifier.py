from enum import Enum


class KitchenSinkBulkProfileBodyProfilesItemProfileIdentifierType2Identifier(str, Enum):
    USERID = "userID"

    def __str__(self) -> str:
        return str(self.value)
