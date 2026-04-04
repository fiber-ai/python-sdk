from enum import Enum


class CombinedSearchCountBodyProfileParamsKeywordsV2Type0Operator(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
