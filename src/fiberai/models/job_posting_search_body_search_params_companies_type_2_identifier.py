from enum import Enum


class JobPostingSearchBodySearchParamsCompaniesType2Identifier(str, Enum):
    LINKEDINURL = "linkedinUrl"

    def __str__(self) -> str:
        return str(self.value)
