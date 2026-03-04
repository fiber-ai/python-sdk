from enum import Enum

class CreateSavedSearchBodySearchParamsType2Type(str, Enum):
    PROFILES = "profiles"

    def __str__(self) -> str:
        return str(self.value)
