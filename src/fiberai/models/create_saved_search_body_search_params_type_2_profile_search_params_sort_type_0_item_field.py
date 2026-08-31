from enum import StrEnum


class CreateSavedSearchBodySearchParamsType2ProfileSearchParamsSortType0ItemField(StrEnum):
    CAREERSTARTEDAT = "careerStartedAt"
    CONNECTIONCOUNT = "connectionCount"
    CURRENTCOMPANYSTARTEDAT = "currentCompanyStartedAt"
    CURRENTROLESTARTEDAT = "currentRoleStartedAt"
    DATAUPDATEDAT = "dataUpdatedAt"
    FOLLOWERCOUNT = "followerCount"
    JOBCOUNT = "jobCount"

    def __str__(self) -> str:
        return str(self.value)
