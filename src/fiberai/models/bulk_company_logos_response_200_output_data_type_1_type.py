from enum import Enum


class BulkCompanyLogosResponse200OutputDataType1Type(str, Enum):
    LINKEDINURLS = "linkedinUrls"

    def __str__(self) -> str:
        return str(self.value)
