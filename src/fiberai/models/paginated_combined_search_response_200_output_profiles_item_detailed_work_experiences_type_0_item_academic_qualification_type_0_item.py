from enum import StrEnum


class PaginatedCombinedSearchResponse200OutputProfilesItemDetailedWorkExperiencesType0ItemAcademicQualificationType0Item(
    StrEnum
):
    ASSOCIATE_DEGREE = "Associate Degree"
    BACHELOR_DEGREE = "Bachelor Degree"
    HIGH_SCHOOL = "High School"

    def __str__(self) -> str:
        return str(self.value)
