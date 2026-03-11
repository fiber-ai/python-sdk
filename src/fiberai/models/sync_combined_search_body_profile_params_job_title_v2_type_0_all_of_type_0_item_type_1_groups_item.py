from enum import Enum


class SyncCombinedSearchBodyProfileParamsJobTitleV2Type0AllOfType0ItemType1GroupsItem(str, Enum):
    BOARD_MEMBER = "board-member"
    C_SUITE = "c-suite"
    FOUNDER = "founder"

    def __str__(self) -> str:
        return str(self.value)
