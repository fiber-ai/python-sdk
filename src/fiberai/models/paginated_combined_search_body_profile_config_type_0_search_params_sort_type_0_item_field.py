from enum import Enum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsSortType0ItemField(str, Enum):
    CAREERSTARTEDAT = "careerStartedAt"
    CONNECTIONCOUNT = "connectionCount"
    CURRENTCOMPANYSTARTEDAT = "currentCompanyStartedAt"
    CURRENTROLESTARTEDAT = "currentRoleStartedAt"
    DATAUPDATEDAT = "dataUpdatedAt"
    FOLLOWERCOUNT = "followerCount"
    JOBCOUNT = "jobCount"

    def __str__(self) -> str:
        return str(self.value)
