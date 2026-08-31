from enum import StrEnum


class CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingsV2Type0AllOfType0ItemJobLocationTypeType0Item(
    StrEnum
):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
