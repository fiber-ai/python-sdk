from enum import StrEnum


class PeopleSearchBodySearchParamsJobStatusType1Status(StrEnum):
    PREVIOUSLY_EMPLOYED = "previously-employed"

    def __str__(self) -> str:
        return str(self.value)
