from enum import StrEnum


class ReverseEmailLookupResponse200OutputDataItemDetailedWorkExperiencesType0ItemSeniorityType1(StrEnum):
    ASSOCIATE = "Associate"
    DIRECTOR = "Director"
    ENTRY_LEVEL = "Entry level"
    EXECUTIVE = "Executive"
    INTERNSHIP = "Internship"
    MID_SENIOR_LEVEL = "Mid-Senior level"

    def __str__(self) -> str:
        return str(self.value)
