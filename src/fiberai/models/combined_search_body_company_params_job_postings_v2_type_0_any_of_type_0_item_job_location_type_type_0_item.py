from enum import Enum

class CombinedSearchBodyCompanyParamsJobPostingsV2Type0AnyOfType0ItemJobLocationTypeType0Item(str, Enum):
    HYBRID = "Hybrid"
    ON_SITE = "On-site"
    REMOTE = "Remote"

    def __str__(self) -> str:
        return str(self.value)
