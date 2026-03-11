from enum import Enum


class JobPostingSearchCountBodySearchParamsCompaniesType3Identifier(str, Enum):
    LINKEDINORGID = "linkedinOrgID"

    def __str__(self) -> str:
        return str(self.value)
