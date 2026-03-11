from enum import Enum


class PeopleSearchBodySearchParamsLeftStealthAtType1Strategy(str, Enum):
    RELATIVE = "relative"

    def __str__(self) -> str:
        return str(self.value)
