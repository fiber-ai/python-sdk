from enum import StrEnum


class GetCurrentCompaniesInSavedSearchBodyStatusesType0Item(StrEnum):
    DEPARTED = "departed"
    JOINED = "joined"
    RETURNED = "returned"
    STAYED = "stayed"

    def __str__(self) -> str:
        return str(self.value)
