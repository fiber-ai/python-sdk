from enum import Enum


class QuickPersonResolveBodyPeopleItemType3Identifier(str, Enum):
    ENTITYURN = "entityUrn"

    def __str__(self) -> str:
        return str(self.value)
