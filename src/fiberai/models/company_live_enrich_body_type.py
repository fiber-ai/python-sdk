from enum import Enum

class CompanyLiveEnrichBodyType(str, Enum):
    LIURL = "liUrl"
    ORGID = "orgId"
    SLUG = "slug"

    def __str__(self) -> str:
        return str(self.value)
