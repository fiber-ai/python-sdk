from enum import StrEnum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingsV2Type0AllOfType0ItemSeniorityType0Item(
    StrEnum
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
