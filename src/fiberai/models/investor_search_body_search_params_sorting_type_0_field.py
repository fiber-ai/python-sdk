from enum import Enum


class InvestorSearchBodySearchParamsSortingType0Field(str, Enum):
    FOUNDED_ON = "founded_on"
    IMPORTANCE = "importance"
    LAST_INVESTMENT_DATE = "last_investment_date"
    LEAD_INVESTMENT_COUNT = "lead_investment_count"
    LEAD_INVESTMENT_RATE = "lead_investment_rate"
    NAME = "name"
    TOTAL_INVESTMENT_COUNT = "total_investment_count"

    def __str__(self) -> str:
        return str(self.value)
