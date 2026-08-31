from enum import StrEnum


class GetTalentFlowBodyCompanyType2Identifier(StrEnum):
    LINKEDINORGID = "linkedinOrgId"

    def __str__(self) -> str:
        return str(self.value)
