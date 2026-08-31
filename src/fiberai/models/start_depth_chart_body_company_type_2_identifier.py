from enum import StrEnum


class StartDepthChartBodyCompanyType2Identifier(StrEnum):
    LINKEDINORGID = "linkedinOrgId"

    def __str__(self) -> str:
        return str(self.value)
