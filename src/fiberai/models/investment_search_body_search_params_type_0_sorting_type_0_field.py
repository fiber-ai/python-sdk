from enum import Enum

class InvestmentSearchBodySearchParamsType0SortingType0Field(str, Enum):
    COMPANY_NAME = "company_name"
    INVESTOR_NAME = "investor_name"
    RAISED_AMOUNT_USD = "raised_amount_usd"
    ROUND_DATE = "round_date"

    def __str__(self) -> str:
        return str(self.value)
