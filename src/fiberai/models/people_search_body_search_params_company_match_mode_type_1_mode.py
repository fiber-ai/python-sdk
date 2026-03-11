from enum import Enum


class PeopleSearchBodySearchParamsCompanyMatchModeType1Mode(str, Enum):
    LOOSE = "loose"

    def __str__(self) -> str:
        return str(self.value)
