from enum import Enum


class ReverseEmailLookupResponse200OutputDataItemExperiencesType0ItemSeniorityType1(str, Enum):
    ASSOCIATE = "Associate"
    DIRECTOR = "Director"
    ENTRY_LEVEL = "Entry level"
    EXECUTIVE = "Executive"
    INTERNSHIP = "Internship"
    MID_SENIOR_LEVEL = "Mid-Senior level"

    def __str__(self) -> str:
        return str(self.value)
