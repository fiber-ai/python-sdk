from enum import StrEnum


class CreateTrackerCompanyListBodyCompanySearchParamsType0JobPostingsV2Type0NoneOfType0ItemJobLocationTypeType0Item(
    StrEnum
):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
