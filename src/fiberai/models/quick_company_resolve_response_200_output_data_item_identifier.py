from enum import Enum


class QuickCompanyResolveResponse200OutputDataItemIdentifier(str, Enum):
    DOMAIN = "domain"
    LINKEDINORGID = "linkedinOrgId"
    LINKEDINSLUG = "linkedinSlug"
    LINKEDINURL = "linkedinUrl"

    def __str__(self) -> str:
        return str(self.value)
