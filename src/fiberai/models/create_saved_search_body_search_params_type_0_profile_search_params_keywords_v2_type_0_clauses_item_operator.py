from enum import Enum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsKeywordsV2Type0ClausesItemOperator(str, Enum):
    AND = "AND"
    OR = "OR"

    def __str__(self) -> str:
        return str(self.value)
