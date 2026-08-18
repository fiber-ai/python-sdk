from enum import Enum


class GetTalentFlowBodyCompanyType2Identifier(str, Enum):
    LINKEDINORGID = "linkedinOrgId"

    def __str__(self) -> str:
        return str(self.value)
