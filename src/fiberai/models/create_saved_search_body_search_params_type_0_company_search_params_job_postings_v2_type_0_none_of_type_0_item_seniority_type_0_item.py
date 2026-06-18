from enum import Enum


class CreateSavedSearchBodySearchParamsType0CompanySearchParamsJobPostingsV2Type0NoneOfType0ItemSeniorityType0Item(
    str, Enum
):
    ASSOCIATE = "Associate"
    DIRECTOR = "Director"
    ENTRY_LEVEL = "Entry level"
    EXECUTIVE = "Executive"
    INTERNSHIP = "Internship"
    MID_SENIOR_LEVEL = "Mid-Senior level"
    NOT_APPLICABLE = "Not Applicable"

    def __str__(self) -> str:
        return str(self.value)
