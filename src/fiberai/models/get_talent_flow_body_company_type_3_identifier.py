from enum import Enum


class GetTalentFlowBodyCompanyType3Identifier(str, Enum):
    DOMAIN = "domain"

    def __str__(self) -> str:
        return str(self.value)
