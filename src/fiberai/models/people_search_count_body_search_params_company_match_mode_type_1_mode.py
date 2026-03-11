from enum import Enum


class PeopleSearchCountBodySearchParamsCompanyMatchModeType1Mode(str, Enum):
    LOOSE = "loose"

    def __str__(self) -> str:
        return str(self.value)
