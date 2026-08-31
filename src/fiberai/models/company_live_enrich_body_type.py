from enum import StrEnum


class CompanyLiveEnrichBodyType(StrEnum):
    LIURL = "liUrl"
    ORGID = "orgId"
    SLUG = "slug"

    def __str__(self) -> str:
        return str(self.value)
