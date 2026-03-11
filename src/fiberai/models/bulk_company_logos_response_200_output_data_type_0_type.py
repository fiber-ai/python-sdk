from enum import Enum


class BulkCompanyLogosResponse200OutputDataType0Type(str, Enum):
    DOMAINS = "domains"

    def __str__(self) -> str:
        return str(self.value)
