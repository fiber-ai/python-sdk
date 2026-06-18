from enum import Enum


class CreateSavedSearchBodySearchParamsType1CompanySearchParamsJobPostingsV2Type0AnyOfType0ItemEmploymentTypeType0Item(
    str, Enum
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
