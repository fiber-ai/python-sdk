from enum import Enum


class InvestorSearchBodySearchParamsInvestorTypeType2Type1(str, Enum):
    EITHER = "either"
    ORGANIZATION = "organization"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
