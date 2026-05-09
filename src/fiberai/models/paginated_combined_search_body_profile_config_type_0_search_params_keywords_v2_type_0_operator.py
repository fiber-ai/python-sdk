from enum import Enum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsKeywordsV2Type0Operator(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
