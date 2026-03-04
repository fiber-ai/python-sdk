from enum import Enum

class JobPostingSearchBodySearchParamsCompaniesType3Identifier(str, Enum):
    LINKEDINORGID = "linkedinOrgID"

    def __str__(self) -> str:
        return str(self.value)
