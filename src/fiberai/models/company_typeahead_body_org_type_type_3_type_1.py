from enum import Enum

class CompanyTypeaheadBodyOrgTypeType3Type1(str, Enum):
    INVESTOR = "investor"
    SCHOOL = "school"

    def __str__(self) -> str:
        return str(self.value)
