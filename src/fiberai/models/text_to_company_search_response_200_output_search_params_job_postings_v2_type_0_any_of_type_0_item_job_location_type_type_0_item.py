from enum import Enum


class TextToCompanySearchResponse200OutputSearchParamsJobPostingsV2Type0AnyOfType0ItemJobLocationTypeType0Item(
    str, Enum
):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
