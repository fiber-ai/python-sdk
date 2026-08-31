from enum import StrEnum


class PeopleSearchCountBodySearchParamsJobTitleV2Type0AllOfType0ItemType2GroupsItem(StrEnum):
    ASSISTANT = "assistant"
    DIRECTOR = "director"
    ENTRY_LEVEL = "entry-level"
    INTERN = "intern"
    MANAGEMENT = "management"
    VP = "vp"

    def __str__(self) -> str:
        return str(self.value)
