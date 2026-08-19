from enum import Enum


class QuickCompanyResolveBodyCompaniesItemType2Identifier(str, Enum):
    LINKEDINORGID = "linkedinOrgId"

    def __str__(self) -> str:
        return str(self.value)
