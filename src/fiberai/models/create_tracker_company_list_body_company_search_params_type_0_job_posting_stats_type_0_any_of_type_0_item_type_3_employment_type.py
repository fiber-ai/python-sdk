from enum import StrEnum


class CreateTrackerCompanyListBodyCompanySearchParamsType0JobPostingStatsType0AnyOfType0ItemType3EmploymentType(
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
