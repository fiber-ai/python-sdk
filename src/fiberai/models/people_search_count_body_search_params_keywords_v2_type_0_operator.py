from enum import Enum


class PeopleSearchCountBodySearchParamsKeywordsV2Type0Operator(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
