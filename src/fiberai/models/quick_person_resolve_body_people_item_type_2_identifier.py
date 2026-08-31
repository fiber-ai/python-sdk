from enum import StrEnum


class QuickPersonResolveBodyPeopleItemType2Identifier(StrEnum):
    LINKEDINUSERID = "linkedinUserId"

    def __str__(self) -> str:
        return str(self.value)
