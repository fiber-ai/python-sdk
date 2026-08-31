from enum import StrEnum


class BulkCompanyLogosResponse200OutputDataType2Type(StrEnum):
    LIORGIDS = "liOrgIds"

    def __str__(self) -> str:
        return str(self.value)
