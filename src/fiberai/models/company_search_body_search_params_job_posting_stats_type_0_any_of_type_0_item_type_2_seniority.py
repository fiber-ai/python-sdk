from enum import Enum


class CompanySearchBodySearchParamsJobPostingStatsType0AnyOfType0ItemType2Seniority(str, Enum):
    ASSOCIATE = "Associate"
    DIRECTOR = "Director"
    ENTRY_LEVEL = "Entry level"
    EXECUTIVE = "Executive"
    INTERNSHIP = "Internship"
    MID_SENIOR_LEVEL = "Mid-Senior level"
    NOT_APPLICABLE = "Not Applicable"

    def __str__(self) -> str:
        return str(self.value)
