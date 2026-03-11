from enum import Enum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsJobPostingsV2Type0AllOfType0ItemJobLocationTypeType0Item(
    str, Enum
):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
