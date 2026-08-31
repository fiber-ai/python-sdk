from enum import StrEnum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0AllOfType0ItemType2Seniority(
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
