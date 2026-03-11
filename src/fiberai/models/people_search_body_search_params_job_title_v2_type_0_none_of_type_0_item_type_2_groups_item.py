from enum import Enum


class PeopleSearchBodySearchParamsJobTitleV2Type0NoneOfType0ItemType2GroupsItem(str, Enum):
    ASSISTANT = "assistant"
    DIRECTOR = "director"
    ENTRY_LEVEL = "entry-level"
    INTERN = "intern"
    MANAGEMENT = "management"
    VP = "vp"

    def __str__(self) -> str:
        return str(self.value)
