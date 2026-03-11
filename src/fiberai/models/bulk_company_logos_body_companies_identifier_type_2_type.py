from enum import Enum


class BulkCompanyLogosBodyCompaniesIdentifierType2Type(str, Enum):
    LIORGIDS = "liOrgIds"

    def __str__(self) -> str:
        return str(self.value)
