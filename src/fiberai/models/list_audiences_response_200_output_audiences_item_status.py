from enum import Enum


class ListAudiencesResponse200OutputAudiencesItemStatus(str, Enum):
    BUILDING = "BUILDING"
    DRAFT = "DRAFT"
    FAILED = "FAILED"
    HEALING_COMPANIES = "HEALING_COMPANIES"
    LINKING_PROSPECTS_WITH_COMPANIES = "LINKING_PROSPECTS_WITH_COMPANIES"
    NORMAL = "NORMAL"
    SAVING_COMPANIES = "SAVING_COMPANIES"
    SAVING_PROSPECTS = "SAVING_PROSPECTS"

    def __str__(self) -> str:
        return str(self.value)
