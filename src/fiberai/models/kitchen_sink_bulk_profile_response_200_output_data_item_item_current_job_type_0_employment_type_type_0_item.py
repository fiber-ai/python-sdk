from enum import StrEnum


class KitchenSinkBulkProfileResponse200OutputDataItemItemCurrentJobType0EmploymentTypeType0Item(StrEnum):
    CONTRACT = "Contract"
    FULL_TIME = "Full-time"
    INTERNSHIP = "Internship"
    OTHER = "Other"
    PART_TIME = "Part-time"
    TEMPORARY = "Temporary"
    VOLUNTEER = "Volunteer"

    def __str__(self) -> str:
        return str(self.value)
