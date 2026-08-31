from enum import StrEnum


class CompanySearchBodySearchParamsTagsType0NoneOfType0Item(StrEnum):
    IS_GOVERNMENT = "is-government"
    IS_SCHOOL = "is-school"
    RAISED_FROM_TOP_VC = "raised-from-top-vc"
    VENTURE_BACKED_STARTUP = "venture-backed-startup"

    def __str__(self) -> str:
        return str(self.value)
