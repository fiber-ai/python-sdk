from enum import StrEnum


class GetDepartmentSizeBodyCompanyType3Identifier(StrEnum):
    DOMAIN = "domain"

    def __str__(self) -> str:
        return str(self.value)
