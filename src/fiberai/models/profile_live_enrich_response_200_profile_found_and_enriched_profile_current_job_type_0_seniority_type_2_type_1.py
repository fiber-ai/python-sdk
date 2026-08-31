from enum import StrEnum


class ProfileLiveEnrichResponse200ProfileFoundAndEnrichedProfileCurrentJobType0SeniorityType2Type1(StrEnum):
    ASSOCIATE = "Associate"
    DIRECTOR = "Director"
    ENTRY_LEVEL = "Entry level"
    EXECUTIVE = "Executive"
    INTERNSHIP = "Internship"
    MID_SENIOR_LEVEL = "Mid-Senior level"

    def __str__(self) -> str:
        return str(self.value)
