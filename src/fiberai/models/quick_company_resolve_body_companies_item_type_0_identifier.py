from enum import Enum


class QuickCompanyResolveBodyCompaniesItemType0Identifier(str, Enum):
    LINKEDINURL = "linkedinUrl"

    def __str__(self) -> str:
        return str(self.value)
