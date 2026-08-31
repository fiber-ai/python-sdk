from enum import StrEnum


class QuickCompanyResolveBodyCompaniesItemType1Identifier(StrEnum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
