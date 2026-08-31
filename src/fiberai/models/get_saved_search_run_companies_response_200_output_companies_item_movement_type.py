from enum import StrEnum


class GetSavedSearchRunCompaniesResponse200OutputCompaniesItemMovementType(StrEnum):
    DEPARTED = "departed"
    JOINED = "joined"
    RETURNED = "returned"
    STAYED = "stayed"

    def __str__(self) -> str:
        return str(self.value)
