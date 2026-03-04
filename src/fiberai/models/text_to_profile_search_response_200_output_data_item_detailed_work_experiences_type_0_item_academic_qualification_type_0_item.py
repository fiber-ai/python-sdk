from enum import Enum

class TextToProfileSearchResponse200OutputDataItemDetailedWorkExperiencesType0ItemAcademicQualificationType0Item(str, Enum):
    ASSOCIATE_DEGREE = "Associate Degree"
    BACHELOR_DEGREE = "Bachelor Degree"
    HIGH_SCHOOL = "High School"

    def __str__(self) -> str:
        return str(self.value)
