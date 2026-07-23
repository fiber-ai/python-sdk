from enum import Enum


class CreateSavedSearchBodySearchParamsType0ProfileSearchParamsEducationV2Type0AnyOfType0ItemYearsType0FinishedSchoolAtType1WindowType2Which(
    str, Enum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
