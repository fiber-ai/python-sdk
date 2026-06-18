from enum import Enum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsPastJobTextType0Joiner(str, Enum):
    AND = "and"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
