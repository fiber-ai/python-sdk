from enum import StrEnum


class ReversePhoneLookupResponse200OutputResultsItemType0ProfileExperiencesType0ItemSeniorityType2Type1(StrEnum):
    ASSOCIATE = "Associate"
    DIRECTOR = "Director"
    ENTRY_LEVEL = "Entry level"
    EXECUTIVE = "Executive"
    INTERNSHIP = "Internship"
    MID_SENIOR_LEVEL = "Mid-Senior level"

    def __str__(self) -> str:
        return str(self.value)
