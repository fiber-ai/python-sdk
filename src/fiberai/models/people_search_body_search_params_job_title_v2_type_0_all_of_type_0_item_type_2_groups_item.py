from enum import Enum

class PeopleSearchBodySearchParamsJobTitleV2Type0AllOfType0ItemType2GroupsItem(str, Enum):
    ASSISTANT = "assistant"
    DIRECTOR = "director"
    ENTRY_LEVEL = "entry-level"
    INTERN = "intern"
    MANAGEMENT = "management"
    VP = "vp"

    def __str__(self) -> str:
        return str(self.value)
