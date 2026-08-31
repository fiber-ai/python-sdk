from enum import StrEnum


class PeopleSearchCountBodySearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1WindowType2Which(
    StrEnum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
