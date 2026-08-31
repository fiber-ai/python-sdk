from enum import StrEnum


class ReversePhoneLookupResponse200OutputResultsItemType0ProfileExperiencesType0ItemAcademicQualificationType0Item(
    StrEnum
):
    ASSOCIATE_DEGREE = "Associate Degree"
    BACHELOR_DEGREE = "Bachelor Degree"
    HIGH_SCHOOL = "High School"

    def __str__(self) -> str:
        return str(self.value)
