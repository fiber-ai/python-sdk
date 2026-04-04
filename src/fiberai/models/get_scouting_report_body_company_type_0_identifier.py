from enum import Enum


class GetScoutingReportBodyCompanyType0Identifier(str, Enum):
    LINKEDINURL = "linkedinUrl"

    def __str__(self) -> str:
        return str(self.value)
