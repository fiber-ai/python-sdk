from enum import Enum


class BulkCompanyLogosBodyCompaniesIdentifierType1Type(str, Enum):
    LINKEDINURLS = "linkedinUrls"

    def __str__(self) -> str:
        return str(self.value)
