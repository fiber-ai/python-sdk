from enum import Enum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsSortType0ItemField(str, Enum):
    EMPLOYEECOUNT = "employeeCount"
    FOLLOWERCOUNT = "followerCount"
    FOUNDEDAT = "foundedAt"
    JOBPOSTINGCOUNT = "jobPostingCount"
    LASTFUNDEDAT = "lastFundedAt"
    LASTROUNDFUNDING = "lastRoundFunding"
    REVENUEESTIMATE = "revenueEstimate"
    TOTALFUNDING = "totalFunding"

    def __str__(self) -> str:
        return str(self.value)
