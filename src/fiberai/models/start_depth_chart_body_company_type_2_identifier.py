from enum import Enum


class StartDepthChartBodyCompanyType2Identifier(str, Enum):
    LINKEDINORGID = "linkedinOrgId"

    def __str__(self) -> str:
        return str(self.value)
