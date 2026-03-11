from enum import Enum


class PeopleSearchCountBodySearchParamsJobTitleV3Type0AllOfType0ItemType1SeniorityItem(str, Enum):
    C_SUITE = "c-suite"
    DIRECTOR = "director"
    HEAD = "head"
    LEAD = "lead"
    MANAGER = "manager"
    PRINCIPAL = "principal"
    SENIOR = "senior"
    STAFF = "staff"
    SVP = "svp"
    VP = "vp"

    def __str__(self) -> str:
        return str(self.value)
