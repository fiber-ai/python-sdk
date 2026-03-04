from enum import Enum

class GetSavedSearchRunProfilesResponse200OutputProfilesItemProfileExperiencesType0ItemEmploymentTypeType0Item(str, Enum):
    CONTRACT = "Contract"
    FULL_TIME = "Full-time"
    INTERNSHIP = "Internship"
    OTHER = "Other"
    PART_TIME = "Part-time"
    TEMPORARY = "Temporary"
    VOLUNTEER = "Volunteer"

    def __str__(self) -> str:
        return str(self.value)
