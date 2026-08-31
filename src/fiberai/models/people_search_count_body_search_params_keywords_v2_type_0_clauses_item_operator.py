from enum import StrEnum


class PeopleSearchCountBodySearchParamsKeywordsV2Type0ClausesItemOperator(StrEnum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
