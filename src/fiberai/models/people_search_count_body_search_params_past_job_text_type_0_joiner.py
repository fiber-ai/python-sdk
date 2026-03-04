from enum import Enum

class PeopleSearchCountBodySearchParamsPastJobTextType0Joiner(str, Enum):
    AND = "and"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
