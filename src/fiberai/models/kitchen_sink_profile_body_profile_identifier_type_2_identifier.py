from enum import Enum

class KitchenSinkProfileBodyProfileIdentifierType2Identifier(str, Enum):
    USERID = "userID"

    def __str__(self) -> str:
        return str(self.value)
