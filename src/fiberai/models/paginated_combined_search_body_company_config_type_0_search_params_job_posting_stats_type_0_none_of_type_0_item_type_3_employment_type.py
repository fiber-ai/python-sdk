from enum import StrEnum


class PaginatedCombinedSearchBodyCompanyConfigType0SearchParamsJobPostingStatsType0NoneOfType0ItemType3EmploymentType(
    StrEnum
):
    CONTRACT = "Contract"
    FULL_TIME = "Full-time"
    INTERNSHIP = "Internship"
    OTHER = "Other"
    PART_TIME = "Part-time"
    TEMPORARY = "Temporary"
    VOLUNTEER = "Volunteer"

    def __str__(self) -> str:
        return str(self.value)
