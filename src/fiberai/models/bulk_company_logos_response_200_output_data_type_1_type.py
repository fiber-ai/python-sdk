from enum import StrEnum


class BulkCompanyLogosResponse200OutputDataType1Type(StrEnum):
    LINKEDINURLS = "linkedinUrls"

    def __str__(self) -> str:
        return str(self.value)
