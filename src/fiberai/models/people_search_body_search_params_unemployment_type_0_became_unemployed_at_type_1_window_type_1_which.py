from enum import Enum


class PeopleSearchBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which(str, Enum):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
