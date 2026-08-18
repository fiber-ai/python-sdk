from enum import Enum


class GetTalentFlowBodyCompanyType1Identifier(str, Enum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
