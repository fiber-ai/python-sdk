from enum import Enum


class QuickCompanyResolveBodyCompaniesItemType1Identifier(str, Enum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
