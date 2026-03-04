from enum import Enum

class InvestorSearchResponse200OutputInvestorsItemTypeType2Type1(str, Enum):
    ORGANIZATION = "organization"
    PERSON = "person"

    def __str__(self) -> str:
        return str(self.value)
