from enum import StrEnum


class LiteReverseEmailLookupResponse200OutputDataItemExperiencesType0ItemEmploymentTypeType0Item(StrEnum):
    CONTRACT = "Contract"
    FULL_TIME = "Full-time"
    INTERNSHIP = "Internship"
    OTHER = "Other"
    PART_TIME = "Part-time"
    TEMPORARY = "Temporary"
    VOLUNTEER = "Volunteer"

    def __str__(self) -> str:
        return str(self.value)
