from enum import Enum


class QuickPersonResolveBodyPeopleItemType2Identifier(str, Enum):
    LINKEDINUSERID = "linkedinUserId"

    def __str__(self) -> str:
        return str(self.value)
