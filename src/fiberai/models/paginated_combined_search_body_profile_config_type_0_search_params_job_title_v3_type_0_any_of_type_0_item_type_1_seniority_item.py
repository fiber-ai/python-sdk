from enum import StrEnum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsJobTitleV3Type0AnyOfType0ItemType1SeniorityItem(StrEnum):
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
