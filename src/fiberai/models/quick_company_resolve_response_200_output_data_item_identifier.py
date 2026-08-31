from enum import StrEnum


class QuickCompanyResolveResponse200OutputDataItemIdentifier(StrEnum):
    DOMAIN = "domain"
    LINKEDINORGID = "linkedinOrgId"
    LINKEDINSLUG = "linkedinSlug"
    LINKEDINURL = "linkedinUrl"

    def __str__(self) -> str:
        return str(self.value)
