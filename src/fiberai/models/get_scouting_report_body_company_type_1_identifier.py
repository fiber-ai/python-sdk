from enum import Enum


class GetScoutingReportBodyCompanyType1Identifier(str, Enum):
    LINKEDINSLUG = "linkedinSlug"

    def __str__(self) -> str:
        return str(self.value)
