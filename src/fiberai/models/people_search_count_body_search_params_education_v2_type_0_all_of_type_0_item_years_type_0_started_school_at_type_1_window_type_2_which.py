from enum import Enum


class PeopleSearchCountBodySearchParamsEducationV2Type0AllOfType0ItemYearsType0StartedSchoolAtType1WindowType2Which(
    str, Enum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
