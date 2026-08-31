from enum import StrEnum


class PeopleSearchCountBodySearchParamsPastJobTextType0Joiner(StrEnum):
    AND = "and"
    OR = "or"

    def __str__(self) -> str:
        return str(self.value)
