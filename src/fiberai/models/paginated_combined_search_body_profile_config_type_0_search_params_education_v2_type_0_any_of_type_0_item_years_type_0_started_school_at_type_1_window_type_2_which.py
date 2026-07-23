from enum import Enum


class PaginatedCombinedSearchBodyProfileConfigType0SearchParamsEducationV2Type0AnyOfType0ItemYearsType0StartedSchoolAtType1WindowType2Which(
    str, Enum
):
    CURRENT = "current"
    PREVIOUS = "previous"

    def __str__(self) -> str:
        return str(self.value)
