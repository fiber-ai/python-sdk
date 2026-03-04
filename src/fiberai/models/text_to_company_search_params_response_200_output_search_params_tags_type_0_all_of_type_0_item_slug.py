from enum import Enum

class TextToCompanySearchParamsResponse200OutputSearchParamsTagsType0AllOfType0ItemSlug(str, Enum):
    IS_GOVERNMENT = "is-government"
    IS_SCHOOL = "is-school"
    RAISED_FROM_TOP_VC = "raised-from-top-vc"
    VENTURE_BACKED_STARTUP = "venture-backed-startup"

    def __str__(self) -> str:
        return str(self.value)
