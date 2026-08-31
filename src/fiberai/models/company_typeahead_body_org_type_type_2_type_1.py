from enum import StrEnum


class CompanyTypeaheadBodyOrgTypeType2Type1(StrEnum):
    INVESTOR = "investor"
    SCHOOL = "school"

    def __str__(self) -> str:
        return str(self.value)
