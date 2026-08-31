from enum import StrEnum


class PeopleSearchBodySearchParamsKeywordsV2Type0Operator(StrEnum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
