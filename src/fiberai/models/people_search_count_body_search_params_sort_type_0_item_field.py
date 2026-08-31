from enum import StrEnum


class PeopleSearchCountBodySearchParamsSortType0ItemField(StrEnum):
    CAREERSTARTEDAT = "careerStartedAt"
    CONNECTIONCOUNT = "connectionCount"
    CURRENTCOMPANYSTARTEDAT = "currentCompanyStartedAt"
    CURRENTROLESTARTEDAT = "currentRoleStartedAt"
    DATAUPDATEDAT = "dataUpdatedAt"
    FOLLOWERCOUNT = "followerCount"
    JOBCOUNT = "jobCount"

    def __str__(self) -> str:
        return str(self.value)
