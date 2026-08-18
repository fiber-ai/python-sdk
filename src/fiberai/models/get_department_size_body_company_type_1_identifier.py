from enum import Enum


class GetDepartmentSizeBodyCompanyType1Identifier(str, Enum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
