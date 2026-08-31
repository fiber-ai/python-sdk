from enum import StrEnum


class PeopleSearchBodySearchParamsCompanyMatchModeType1Mode(StrEnum):
    LOOSE = "loose"

    def __str__(self) -> str:
        return str(self.value)
