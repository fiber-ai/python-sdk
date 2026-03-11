from enum import Enum


class InvestmentSearchResponse200OutputInvestmentsItemInvestorTypeType1(str, Enum):
    ORGANIZATION = "organization"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
