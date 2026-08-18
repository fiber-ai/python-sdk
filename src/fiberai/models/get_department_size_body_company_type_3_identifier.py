from enum import Enum


class GetDepartmentSizeBodyCompanyType3Identifier(str, Enum):
    DOMAIN = "domain"

    def __str__(self) -> str:
        return str(self.value)
