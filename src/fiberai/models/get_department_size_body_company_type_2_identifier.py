from enum import Enum


class GetDepartmentSizeBodyCompanyType2Identifier(str, Enum):
    LINKEDINORGID = "linkedinOrgId"

    def __str__(self) -> str:
        return str(self.value)
