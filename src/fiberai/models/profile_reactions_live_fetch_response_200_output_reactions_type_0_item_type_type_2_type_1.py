from enum import Enum

class ProfileReactionsLiveFetchResponse200OutputReactionsType0ItemTypeType2Type1(str, Enum):
    CELEBRATE = "CELEBRATE"
    FUNNY = "FUNNY"
    INSIGHTFUL = "INSIGHTFUL"
    LIKE = "LIKE"
    LOVE = "LOVE"
    SUPPORT = "SUPPORT"

    def __str__(self) -> str:
        return str(self.value)
