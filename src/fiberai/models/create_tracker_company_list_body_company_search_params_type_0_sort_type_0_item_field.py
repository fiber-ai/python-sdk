from enum import StrEnum


class CreateTrackerCompanyListBodyCompanySearchParamsType0SortType0ItemField(StrEnum):
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
