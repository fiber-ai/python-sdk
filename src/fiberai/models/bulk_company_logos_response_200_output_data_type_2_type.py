from enum import Enum


class BulkCompanyLogosResponse200OutputDataType2Type(str, Enum):
    LIORGIDS = "liOrgIds"

    def __str__(self) -> str:
        return str(self.value)
