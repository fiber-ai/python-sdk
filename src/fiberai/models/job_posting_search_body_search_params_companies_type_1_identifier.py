from enum import Enum

class JobPostingSearchBodySearchParamsCompaniesType1Identifier(str, Enum):
    DOMAIN = "domain"

    def __str__(self) -> str:
        return str(self.value)
