from enum import Enum


class PeopleSearchCountBodySearchParamsUnemploymentType0BecameUnemployedAtType1WindowType1Which(str, Enum):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
