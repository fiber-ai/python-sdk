from enum import StrEnum


class CompanySearchBodySearchParamsJobPostingsV2Type0AnyOfType0ItemJobLocationTypeType0Item(StrEnum):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
