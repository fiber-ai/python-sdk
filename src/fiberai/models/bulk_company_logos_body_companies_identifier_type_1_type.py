from enum import StrEnum


class BulkCompanyLogosBodyCompaniesIdentifierType1Type(StrEnum):
    LINKEDINURLS = "linkedinUrls"

    def __str__(self) -> str:
        return str(self.value)
