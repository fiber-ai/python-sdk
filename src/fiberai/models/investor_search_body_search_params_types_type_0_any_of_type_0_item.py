from enum import Enum


class InvestorSearchBodySearchParamsTypesType0AnyOfType0Item(str, Enum):
    ACCELERATOR = "accelerator"
    ANGEL = "angel"
    ANGEL_GROUP = "angel_group"
    CORPORATE_VENTURE_CAPITAL = "corporate_venture_capital"
    CO_WORKING_SPACE = "co_working_space"
    ENTREPRENEURSHIP_PROGRAM = "entrepreneurship_program"
    FAMILY_INVESTMENT_OFFICE = "family_investment_office"
    FUND_OF_FUNDS = "fund_of_funds"
    GOVERNMENT_OFFICE = "government_office"
    HEDGE_FUND = "hedge_fund"
    INCUBATOR = "incubator"
    INVESTMENT_BANK = "investment_bank"
    INVESTMENT_PARTNER = "investment_partner"
    MICRO_VC = "micro_vc"
    PENSION_FUNDS = "pension_funds"
    PRIVATE_EQUITY_FIRM = "private_equity_firm"
    SECONDARY_PURCHASER = "secondary_purchaser"
    STARTUP_COMPETITION = "startup_competition"
    SYNDICATE = "syndicate"
    UNIVERSITY_PROGRAM = "university_program"
    VENTURE_CAPITAL = "venture_capital"
    VENTURE_DEBT = "venture_debt"

    def __str__(self) -> str:
        return str(self.value)
