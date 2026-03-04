from enum import Enum

class InvestmentSearchBodySearchParamsType0InvestorTypeType1(str, Enum):
    EITHER = "either"
    ORGANIZATION = "organization"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
