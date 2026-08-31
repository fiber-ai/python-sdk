from enum import StrEnum


class GetScoutingReportBodyCompanyType3Identifier(StrEnum):
    DOMAIN = "domain"

    def __str__(self) -> str:
        return str(self.value)
